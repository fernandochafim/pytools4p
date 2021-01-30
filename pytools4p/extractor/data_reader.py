from typing import List
import pandas as pd
import errno
import os
import glob


def read_data(path: str = None, files: List[str] = None) -> list:
    """Read project data.

        If the argument `path` isn't passed in, the default `../input`
        is used.

        Parameters
        ----------
        path : str, optional
            The relative path where data are stored (default is `../input`)
        
        files, optional
            File names to read

        Raises
        ------
        FileNotFoundError
            If Files or Foulder not found.
    """

    if path == None:
        path = "../input"

    try:
        if files == None:
            all_files = glob.glob(path + "/*.csv")
        else:
            all_files = [path + '/' + s for s in files]
        li = []
        for filename in all_files:
            df = pd.read_csv(filename, index_col=None, header=0)
            li.append(df)
        return li
    except FileNotFoundError:
        print("Files not found. Check the path variable")