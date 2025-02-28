from types import ModuleType
from typing import cast

import pandas as pd
import pandas.testing as pdt
from click import BaseCommand
from click.testing import CliRunner
from pytest_mock import MockerFixture

from csv_getter import CsvGetter


def boilerplate_shared(
        module: ModuleType,
        function: str,
        mocker: MockerFixture,
        df_input: pd.DataFrame,
        df_expected: pd.DataFrame
):
    """Boilerplate for shared test."""
    mocker.patch.object(CsvGetter, "__enter__", return_value=df_input)
    spy = mocker.spy(module, function)
    mocker.patch.object(CsvGetter, "__exit__")
    mocker.patch.object(module.click.Path, "convert")

    runner = CliRunner()
    result = runner.invoke(
        cast(BaseCommand, module.main),
        ["--infile", "in.csv", "--out", "out.csv"]
    )

    assert result.exit_code == 0
    pdt.assert_frame_equal(spy.spy_return, df_expected)
