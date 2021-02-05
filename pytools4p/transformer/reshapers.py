import pandas as pd

def reshaper(df: pd.DataFrame, index_col=None, value_vars=None, var_name = 'day', value_col="value", type = "melt") -> pd.DataFrame:
    """Reshape data to melt or pivot table format.

        Parameters
        ----------
        df : DataFrame
            TODO
        
        index_col : str, optional
            TODO
        
        value_vars : str, optional
            TODO
        
        value_name : str, optional
            TODO
        
        value_col : str, optional
            TODO
        
        type : str, optional
            TODO

    """
    if type == "melt":
        df = pd.melt(df,
                  id_vars = index_col,
                  value_vars=value_vars,
                  var_name = var_name, 
                  value_name = value_col)
    elif type == "pivot":
        df = pd.pivot(df,
                  index=index_col, 
                  columns=var_name, 
                  values=value_col
        )
        df.reset_index(level=0, inplace=True)
    return df
