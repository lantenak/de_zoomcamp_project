from pathlib import Path
import pandas as pd
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket
from prefect_gcp import GcpCredentials

@task(retries = 10)
def extract_from_gcs(month : str, year : int, dataset_file: str, user: str) -> Path:
    ''' Download data from GCS '''

    gcs_path = f'data/{dataset_file}.csv'
    gcs_block = GcsBucket.load('protected-areas-bucket')
    gcs_block.get_directory(
        from_path = gcs_path,
        local_path = f'/home/{user}/'
    )
    return Path(f'/home/{user}/{gcs_path}')

@task(log_prints = True)
def not_transform(path: Path) -> pd.DataFrame:
    ''' Read data from GCS into pandas DataFrame '''
    
    df = pd.read_csv(path, lineterminator='\n', compression = 'gzip')
    df = df.astype(str)
    print(f'rows: {len(df)}')
    return df

@task
def write_bq(df : pd.DataFrame, project_id: str) -> None:
    ''' Write DataFrame to BigQuery '''

    gcp_credentials_block = GcpCredentials.load("protected-areas")

    df.to_gbq(
        destination_table = 'protected_areas_raw.protected_areas',
        project_id = f'{project_id}',
        credentials = gcp_credentials_block.get_credentials_from_service_account(),
        chunksize = 100_000,
        if_exists = 'append'
    )

@flow()
def etl_gcs_to_bq() -> None:
    ''' The main ETL function '''

    user = 'lantenak'
    project_id = 'lan10ak'
    month = 'Apr'
    year = 2023
    dataset_file = f'WDPA_{month}{year}_Public_csv'
    dataset_url = f'https://d1gam3xoknrgr2.cloudfront.net/current/WDPA_{month}{year}_Public_csv.zip'

    path = extract_from_gcs(month, year, dataset_file, user)
    df = not_transform(path)
    write_bq(df, project_id)

if __name__ == '__main__':
    etl_gcs_to_bq()
