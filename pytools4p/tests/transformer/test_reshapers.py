from pytools4p.transformer import reshaper
import pandas as pd
import pandas.testing as tm
from pandas.testing import assert_frame_equal
import numpy as np

def test_pivot_reshaper():
    """Test for normal arguments
    """
    def unpivot(frame):
        N, K = frame.shape
        data = {
            "value": frame.to_numpy().ravel("F"),
            "variable": np.asarray(frame.columns).repeat(N),
            "date": np.tile(np.asarray(frame.index), K)
            }
        return pd.DataFrame(data, columns=["date", "variable", "value"])
    df = unpivot(tm.makeTimeDataFrame(3))
    actual = reshaper(df, index_col="date", var_name="variable", value_col="value", type="pivot")
    expected = pd.pivot(df, "time", columns="date", values = "value").reset_index(level=0, inplace=True)
    assert_frame_equal(actual, expected)

def test_melt_reshaper():
    """Test for normal arguments
    """
    def unpivot(frame):
        N, K = frame.shape
        data = {
            "value": frame.to_numpy().ravel("F"),
            "variable": np.asarray(frame.columns).repeat(N),
            "date": np.tile(np.asarray(frame.index), K)
            }
        return pd.DataFrame(data, columns=["date", "variable", "value"])
    df = pd.pivot(unpivot(tm.makeTimeDataFrame(3)), "time", columns="date", values = "value").reset_index(level=0, inplace=True)
    actual = reshaper(df = df, index_col="date", var_name="variable", value_col="value", type="melt")
    expected = pd.melt(df, var_name = "variable", value_name = "value")
    assert_frame_equal(actual, expected)