import pytest
from pathlib import Path
from pytools4p.extractor import read_data
from pytools4p._testing import assert_list_of_frames_equal
from pytools4p.errors import ListElementPositionError
import pandas as pd

TEST_DATA_DIR = Path(__file__).resolve().parent / 'data'

def test_read_data():
    """Test for normal arguments
    """
    mypath = '../extractor/data'
    myfiles = ['iris_train.csv', 'iris_test.csv']
    actual = read_data(path = mypath, files = myfiles)    
    expected = [pd.read_csv(TEST_DATA_DIR / 'data/iris_train.csv'), pd.read_csv('data/iris_test.csv')]
    message = ("the datasets are not the expected")
    assert assert_list_of_frames_equal(actual, expected), message

def test_fileerror_argument():
    """Test for bad arguments
    """
    pass

def test_foldererror_argument():
    """Test for bad arguments
    """
    pass
