from prefect_gcp.credentials import GcpCredentials
from prefect_dbt.cli import BigQueryTargetConfigs, DbtCliProfile, DbtCoreOperation

credentials = GcpCredentials.load("project-creds")
target_configs = BigQueryTargetConfigs(
    schema="protected_areas_dbt",  # also known as dataset
    credentials=credentials,
)
target_configs.save("protected-areas-dbt-target-config", overwrite=True)

dbt_cli_profile = DbtCliProfile(
    name="protected-areas-dbt-cli-profile",
    target="dev",
    target_configs=target_configs,
)
dbt_cli_profile.save("protected-areas-dbt-cli-profile", overwrite=True)