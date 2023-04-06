import pandas as pd
import os
from pathlib import Path
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket
import zipfile as zp

@task(retries = 10)
def fetch(dataset_url: str, dataset_file: str) -> pd.DataFrame:
    ''' Read data from web into pandas DataFrame '''

    os.system(f'wget {dataset_url}')
    zf = zp.ZipFile(f'{dataset_file}.zip')
    df = pd.read_csv(zf.open(f'{dataset_file}.csv'))
    df = df[['NAME', 'DESIG_ENG', 'STATUS_YR']]
    df = df[df['STATUS_YR'] != 0]
    return df

@task()
def write_local(df : pd.DataFrame, user : str, dataset_file : str) -> Path:
    ''' Write DataFrame out locally as csv file '''
    
    path = Path(f'/home/{user}/data/{dataset_file}.csv')
    df.to_csv(path, compression = 'gzip')
    return path

@task()
def write_gcs(path: Path, dataset_file: str) -> None:
    ''' Upload local csv file to GCS '''

    gcs_block = GcsBucket.load('protected-areas-bucket')
    gcs_block.upload_from_path(
        from_path = path,
        to_path = Path(f'data/{dataset_file}.csv')
    )
    return

@flow()
def etl_web_to_gcs() -> None:
    ''' The main ETL function '''

    user = 'lantenak'
    month = 'Apr'
    year = 2023
    dataset_file = f'WDPA_{month}{year}_Public_csv'
    dataset_url = f'https://d1gam3xoknrgr2.cloudfront.net/current/WDPA_{month}{year}_Public_csv.zip'

    df = fetch(dataset_url, dataset_file)
    path = write_local(df, user, dataset_file)
    write_gcs(path, dataset_file)

if __name__ == '__main__':
    etl_web_to_gcs()
