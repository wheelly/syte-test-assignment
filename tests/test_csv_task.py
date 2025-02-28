from typing import cast

import pandas as pd
import pandas.testing as pdt
import pytest
from click import BaseCommand
from click.testing import CliRunner
from pytest_mock import MockerFixture

import csv_task
from csv_getter import CsvGetter


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
    mocker.patch.object(CsvGetter, "__enter__", return_value=df_input)
    spy = mocker.spy(csv_task, "transform_csv_task")
    mocker.patch.object(CsvGetter, "__exit__")
    mocker.patch.object(csv_task.click.Path, "convert")

    runner = CliRunner()
    result = runner.invoke(
        cast(BaseCommand, csv_task.main),
        ["--infile", "in.csv", "--out", "out.csv"]
    )

    assert result.exit_code == 0
    pdt.assert_frame_equal(spy.spy_return, df_expected)
