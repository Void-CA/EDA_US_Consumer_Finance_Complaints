# test_utility.py
import pandas as pd
import pytest
from scripts.utility import set_column_datatype, set_multiple_columns_datatype, conversion_functions

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        'int_column': ['1', '2', '3', '4'],
        'float_column': ['1.1', '2.2', '3.3', '4.4'],
        'bool_column': ['Yes', 'No', 'yes', 'no'],
        'category_column': ['a', 'b', 'a', 'b'],
        'datetime_column': ['2021-01-01', '2021-02-01', '2021-03-01', '2021-04-01'],
        'string_column': [1, 2, 3, 4]
    })


def test_set_column_datatype_int(sample_df):
    df = set_column_datatype(sample_df, 'int_column', 'int')
    assert df['int_column'].dtype.name == 'Int64'
    assert df['int_column'].iloc[0] == 1


def test_set_column_datatype_float(sample_df):
    df = set_column_datatype(sample_df, 'float_column', 'float')
    assert df['float_column'].dtype.name == 'float64'
    assert df['float_column'].iloc[0] == 1.1


def test_set_column_datatype_bool(sample_df):
    df = set_column_datatype(sample_df, 'bool_column', 'bool')
    assert df['bool_column'].dtype.name == 'bool'
    assert df['bool_column'].iloc[0] == True


def test_set_column_datatype_category(sample_df):
    df = set_column_datatype(sample_df, 'category_column', 'category')
    assert df['category_column'].dtype.name == 'category'
    assert df['category_column'].cat.categories.tolist() == ['a', 'b']


def test_set_column_datatype_datetime(sample_df):
    df = set_column_datatype(sample_df, 'datetime_column', 'datetime')
    assert df['datetime_column'].dtype.name == 'datetime64[ns]'
    assert df['datetime_column'].iloc[0] == pd.Timestamp('2021-01-01')


def test_set_column_datatype_string(sample_df):
    df = set_column_datatype(sample_df, 'string_column', 'string')
    assert df['string_column'].dtype.name == 'object'
    assert df['string_column'].iloc[0] == '1'


def test_set_multiple_columns_datatype(sample_df):
    dtype_dict = {
        'int_column': 'int',
        'float_column': 'float',
        'bool_column': 'bool',
        'category_column': 'category',
        'datetime_column': 'datetime',
        'string_column': 'string'
    }
    df = set_multiple_columns_datatype(sample_df, dtype_dict)

    assert df['int_column'].dtype.name == 'Int64'
    assert df['float_column'].dtype.name == 'float64'
    assert df['bool_column'].dtype.name == 'bool'
    assert df['category_column'].dtype.name == 'category'
    assert df['datetime_column'].dtype.name == 'datetime64[ns]'
    assert df['string_column'].dtype.name == 'object'
