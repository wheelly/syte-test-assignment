import pandas as pd
import pytest
from pytest_mock import MockerFixture
from unit.common import boilerplate_shared

import csv_task


@pytest.mark.parametrize(
    "df_input, df_expected",
    [
        (
            pd.DataFrame({
                "product_name": [
                    "woman's best fit",
                    "Sweater shirt",
                    "Ankle boots"
                ],
                "search_price": [
                    100,
                    200,
                    300
                ]
            }),
            pd.DataFrame({
                "product_name": [
                    "woman's best fit",
                    "Sweater shirt",
                    "Ankle boots"
                ],
                "search_price": [
                    100,
                    200,
                    300
                ],
                "price_edited": [
                    100.0,
                    200.0,
                    300.0
                ],
            }),
        )
    ]
)
def test_csv_task(mocker: MockerFixture, df_input: pd.DataFrame, df_expected: pd.DataFrame):
    """Tests add column from the existing one."""
    boilerplate_shared(csv_task, "transform_csv_task", mocker, df_input, df_expected)
