from pytools4p.errors import ListElementPositionError
from pandas.testing import assert_frame_equal

def assert_list_of_frames_equal(left, right):
    """
     Check that left and right List of DataFrames are equal.
     
     Parameters
    ----------
    left : List of Dataframes
    right : List of Dataframes

    Examples
    --------
    >>> from pandas.testing import assert_series_equal
    >>> a = pd.Series([1, 2, 3, 4])
    >>> b = pd.Series([5, 6, 7, 8])
    >>> list_1 = [a, b]
    >>> c = pd.Series([1, 2, 3, 4])
    >>> d = pd.Series([5, 6, 7, 8])
    >>> list_2 = [c, d]
    >>> assert_series_equal(list_1, list_2)
    """
    result = []
    for x in range(len(left)):
        try:
            assert_frame_equal(left[x], right[x])
            result.append(True)
        except:
            result.append(False)
    if not all(result):
        raise ListElementPositionError(result = result)


