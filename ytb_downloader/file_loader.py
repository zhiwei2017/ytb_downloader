"""Load information from csv file for bulk downloading and converting."""
import logging
import numpy as np
import pandas as pd  # type: ignore
from typing import Sequence, Union, Tuple, List, Dict
from .config import settings

logger = logging.getLogger(settings.PROJECT_SLUG)
DOWNLOADING_FUNC_PARAM = "url"
COL_TYPE_DICT = {"url": str, "format": str, "time_start": "int64",
                 "time_end": str, "fps": int, "bitrate": str}


def columns_validation(columns: Sequence[str]) -> Union[List[str], None]:
    """Validate columns of dataframe read from csv file.

    To make sure the requisite column url exists, and find out existed optional
    columns, such as "format", "time_start", "time_end", "bitrate".

    Args:
        columns (:obj:`list` of :obj:`str`): column names of dataframe read
          from csv file.

    Returns:
        :obj:`None` or :obj:`list` of :obj:`str`: return None if "url" is not
        included in the columns; otherwise return the list of existed optional
        columns.
    """
    converting_func_params = set(COL_TYPE_DICT.keys())
    converting_func_params.remove(DOWNLOADING_FUNC_PARAM)
    if DOWNLOADING_FUNC_PARAM not in columns:
        return None
    return list(converting_func_params.intersection(columns))


def load_file(file_path: str) -> Tuple[List[str], List[Dict]]:
    """Load information from csv file for downloading video function and converting
    video function.

    Args:
        file_path (:obj:`str`): path to the csv file containing information for
          downloading video function and converting video function.

    Returns:
        :obj:`tuple` (:obj:`list` of :obj:`str` and :obj:`list` of :obj:`dict`):
        urls for downloading videos as a list and converting function params as
        a list of dictionaries.
    """
    df = pd.read_csv(file_path, sep=",", dtype=COL_TYPE_DICT)
    converting_func_params = columns_validation(df.columns)
    converting_info_dicts: List[Dict] = []
    if converting_func_params is None:
        logger.error("The requisite column [url] is not in the csv file.")
        raise ValueError("Missing column [url] in csv file.")
    elif not converting_func_params:
        pass
    elif "time_end" in converting_func_params:
        df["time_end"] = df["time_end"].replace(np.nan, None)
        for info_dict in df[converting_func_params].to_dict('records'):
            if info_dict["time_end"]:
                info_dict["time_end"] = int(info_dict["time_end"])
            converting_info_dicts.append(info_dict)
    else:
        converting_info_dicts = df[converting_func_params].to_dict('records')
    return df[DOWNLOADING_FUNC_PARAM].tolist(), converting_info_dicts
