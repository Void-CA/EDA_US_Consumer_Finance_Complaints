from pandas import DataFrame
import pandas as pd

conversion_functions = {
    'int': lambda series: pd.to_numeric(series, errors='coerce').astype('Int64'),
    'float': lambda series: pd.to_numeric(series, errors='coerce'),
    'bool': lambda series: series.map(
        {'Yes': True, 'No': False, 'yes': True, 'no': False, 'true': True, 'false': False, 'True': True,
         'False': False}).astype('bool'),
    'category': lambda series: series.astype('category'),
    'datetime': lambda series: pd.to_datetime(series, errors='coerce'),
    'string': lambda series: series.astype('str')
}


def set_column_datatype(df: DataFrame, column: str, datatype: str) -> DataFrame:
    """
    Set the datatype of a specific column in a DataFrame.

    Parameters:
    df (DataFrame): The DataFrame containing the column.
    column (str): The name of the column to convert.
    datatype (str): The datatype to convert the column to. Supported values are 'int', 'float', 'bool', 'category', 'datetime'.

    Returns:
    DataFrame: The DataFrame with the converted column.
    """
    if datatype in conversion_functions:
        df[column] = conversion_functions[datatype](df[column])
    else:
        raise ValueError(f"Unsupported datatype: {datatype}")
    return df


def set_multiple_columns_datatype(df: DataFrame, columns: dict) -> DataFrame:
    """
    Set the datatype of multiple columns in a DataFrame.

    Parameters:
    df (DataFrame): The DataFrame containing the columns.
    columns (dict): A dictionary where keys are column names and values are the datatypes to convert to.

    Returns:
    DataFrame: The DataFrame with the converted columns.
    """
    for column, datatype in columns.items():
        df = set_column_datatype(df, column, datatype)
    return df
