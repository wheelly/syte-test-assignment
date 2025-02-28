import os
import tempfile

import pytest


@pytest.fixture(scope="session")
def temp_tsv_file():
    # Create a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".tsv")
    try:
        # Write TSV data to the file
        with open(temp_file.name, 'w') as f:
            f.write("column1\tcolumn2\tcolumn3\n")
            f.write("value1\tvalue2\tvalue3\n")
            f.write("value4\tvalue5\tvalue6\n")

        # Yield the file path to the test
        yield temp_file.name
    finally:
        # Delete the temporary file
        os.remove(temp_file.name)
