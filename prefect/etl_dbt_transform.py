from prefect import task, flow
from prefect_dbt.cli import DbtCoreOperation, DbtCliProfile

@flow
def trigger_dbt_flow() -> object:
    """ Triggers the dbt dependency and build commands """

    dbt_cli_profile = DbtCliProfile.load("protected-areas-dbt-cli-profile")

    with DbtCoreOperation(
        commands=["dbt deps", "dbt build --select stg_protected_areas.sql --var 'is_test_run: false'"],
        project_dir="~/de_zoomcamp_project/dbt/",
        profiles_dir="~/de_zoomcamp_project/dbt/",
        # dbt_cli_profile=dbt_cli_profile, # comment out if dbt asks for a dbt_cli_profile
    ) as dbt_operation:
        dbt_process = dbt_operation.trigger()
        dbt_process.wait_for_completion()
        result = dbt_process.fetch_result()
    return result

trigger_dbt_flow()