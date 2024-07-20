import pandas as pd
import pytest
from scripts.utility import (
    set_column_datatype,
    set_multiple_columns_datatype,
    extract_date_features,
    group_rare_categories
)


@pytest.fixture
def sample_df():
    return pd.DataFrame({
        'int_column': ['1', '2', '3', '4', '5', '6'],
        'float_column': ['1.1', '2.2', '3.3', '4.4', '5.5', '6.6'],
        'bool_column': ['Yes', 'No', 'yes', 'no', 'Yes', 'No'],
        'category_column': ['a', 'b', 'c', 'd', 'a', 'b'],
        'category_column_2': ['A', 'B', 'C', 'F', 'A', 'B'],
        'datetime_column': pd.to_datetime([
            '2021-01-01', '2021-02-01', '2021-03-01', '2021-04-01', '2021-05-01', '2021-06-01'
        ]),
        'string_column': ['1', '2', '3', '4', '5', '6']
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
    assert df['bool_column'].iloc[0]


def test_set_column_datatype_category(sample_df):
    df = set_column_datatype(sample_df, 'category_column', 'category')
    assert df['category_column'].dtype.name == 'category'
    assert df['category_column'].cat.categories.tolist() == ['a', 'b', 'c', 'd']


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


def test_group_rare_categories(sample_df):
    df = group_rare_categories(sample_df.copy(), 'category_column', threshold=2)

    # Check if the new column is created
    assert 'category_column_simplified' in df.columns

    # Check the correct grouping
    assert df['category_column_simplified'].iloc[0] == 'a'
    assert df['category_column_simplified'].iloc[1] == 'b'
    assert df['category_column_simplified'].iloc[2] == 'Others'
    assert df['category_column_simplified'].iloc[3] == 'Others'


def test_extract_date_features(sample_df):
    df = extract_date_features(sample_df.copy(), 'datetime_column')

    # Check if the new temporal features are created
    assert 'year_datetime_column' in df.columns
    assert 'month_datetime_column' in df.columns

    # Check some values
    assert df['year_datetime_column'].iloc[0] == 2021
    assert df['month_datetime_column'].iloc[1] == 2
