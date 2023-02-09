from dagster import job, op, get_dagster_logger, asset
import pandas as pd

@asset
def load_df():
    return pd.read_csv('../../data/heart.csv')

@op
def get_median_age(df):
    return df['age'].median()

@op
def get_meadian_chol(df):
    return df['chol'].median()

@op
def print_request_result(result_one, result_two):
    get_dagster_logger().info(f'Requests results: median_chol =  {result_one} and median_age = {result_two}')

@job
def get_start():
    df = load_df()
    age = get_median_age(df)
    chol = get_meadian_chol(df)
    print_request_result(chol, age)
