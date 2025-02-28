import os

import pandas as pd

from src.converter import convert_tsv_to_csv


def test_convert_tsv_to_csv(temp_tsv_file: str):
    """Tests the conversion of a TSV file to a CSV file."""
    # Convert the TSV file to CSV
    convert_tsv_to_csv(temp_tsv_file)

    # Check if the CSV file is created
    csv_file = temp_tsv_file.replace(".tsv", ".csv")
    assert os.path.exists(csv_file)

    # Read the CSV file and compare with the original TSV data
    df_tsv = pd.read_csv(temp_tsv_file, sep="\t")
    df_csv = pd.read_csv(csv_file)
    pd.testing.assert_frame_equal(df_tsv, df_csv)
