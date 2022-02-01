from pprint import pprint

from great_expectations import get_context
from great_expectations.core import ExpectationConfiguration
from great_expectations.core.batch import BatchRequest

context = get_context()
suite = context.create_expectation_suite("flavors_test", overwrite_existing=True)

suite.add_expectation(
    ExpectationConfiguration(
        expectation_type="expect_column_to_exist",
        kwargs={
            "column": "flavor_name",
        },
    )
)

batch_request = BatchRequest(
    datasource_name="my_postgres_db",
    data_asset_name="std.flavors",
    data_connector_name="whole_table",
)

validator = context.get_validator(
    batch_request=batch_request,
    expectation_suite=suite,
)
pprint(validator.validate())
