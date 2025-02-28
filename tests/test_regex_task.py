from typing import cast

import pandas as pd
import pandas.testing as pdt
import pytest
from click import BaseCommand
from click.testing import CliRunner
from pytest_mock import MockerFixture

import regex_task
from csv_getter import CsvGetter


@pytest.mark.parametrize(
    "df_input, df_expected",
    [(
        pd.DataFrame({
            "product_name": ["woman's best fit", "Sweater shirt", "Ankle boots"],
            "description": ["Knitted sweater", "Knitted Sweater with wool", "Cool clothes"],
            "custom5": ["Anything comes best be removed", "Well as soon as jumpers go around it stays", "anything"]
        }),
        pd.DataFrame({
            "product_name": ["Sweater shirt", "Ankle boots"],
            "description": ["Knitted Sweater with wool", "Cool clothes"],
            "custom5": ["Well as soon as jumpers go around it stays", "anything"]
        })
    )]
)
def test_regex_task(mocker: MockerFixture, df_input: pd.DataFrame, df_expected: pd.DataFrame):
    """Test the remove_rows_by_regex function."""
    mocker.patch.object(CsvGetter, "__enter__", return_value=df_input)
    spy = mocker.spy(regex_task, "remove_rows_by_regex")
    mocker.patch.object(CsvGetter, "__exit__")

    runner = CliRunner()
    result = runner.invoke(
        cast(BaseCommand, regex_task.main),
        ["--infile", "in.csv", "--out", "out.csv"]
    )

    assert result.exit_code == 0
    pdt.assert_frame_equal(spy.spy_return, df_expected)
