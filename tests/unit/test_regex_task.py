import pandas as pd
import pytest
from pytest_mock import MockerFixture
from unit.common import boilerplate_shared

import regex_task


@pytest.mark.parametrize(
    "df_input, df_expected",
    [
        (
            pd.DataFrame({
                "product_name": [
                    "woman's best fit",  # row-0 must be removed since without jumpers
                    "Sweater shirt",
                    "Ankle boots"
                ],
                "description": [
                    "Knitted Sweater",  # row-0 must be removed since without jumpers
                    "Knitted Sweater with wool",
                    "Cool clothes"
                ],
                "custom5": [
                    "Anything comes best be removed",  # row-0 must be removed since without jumpers
                    "Well as soon as jumpers go around it stays",
                    "anything"
                ]
            }),
            pd.DataFrame({
                "product_name": [
                    "Sweater shirt",
                    "Ankle boots"
                ],
                "description": [
                    "Knitted Sweater with wool",
                    "Cool clothes"
                ],
                "custom5": [
                    "Well as soon as jumpers go around it stays",
                    "anything"
                ]
            })
        ),
        (
            pd.DataFrame({
                "product_name": [
                    "woman's best fit",
                    "Sweater shirt",  # row-1 must be removed since without jumpers
                    "Ankle boots"
                ],
                "description": [
                    "Knitted Sweater with jumpers",
                    "Knitted Sweater with wool",  # row-1 must be removed since without jumpers
                    "Cool clothes"
                ],
                "custom5": [
                    "Anything comes best be removed",
                    "Well as soon as one jumper go around it goes",  # row-0 must be removed since without jumpers
                    "anything"
                ]
            }),
            pd.DataFrame({
                "product_name": [
                    "woman's best fit",
                    "Ankle boots"
                ],
                "description": [
                    "Knitted Sweater with jumpers",
                    "Cool clothes"
                ],
                "custom5": [
                    "Anything comes best be removed",
                    "anything"
                ]
            })
        ),
    ]
)
def test_regex_task(mocker: MockerFixture, df_input: pd.DataFrame, df_expected: pd.DataFrame):
    """Tests the remove_rows_by_regex function."""
    boilerplate_shared(regex_task, "remove_rows_by_regex", mocker, df_input, df_expected)
