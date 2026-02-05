"""The transform script which takes extracted data from the RTT API and transforms it, ready to load into RDS."""

from logging import getLogger, basicConfig, INFO

import pandas as pd

from extract import extract


def convert_data_to_df(data: list) -> pd.DataFrame:
    """Converts a list of dictionaries to a dataframe."""


if __name__ == "__main__":

    pass
