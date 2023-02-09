from prefect import flow, task
import pandas as pd

@flow
def read_csv(path: str):
    return pd.read_csv(path, index_col=[0])

@task
def get_median(df: pd.DataFrame, column: str):
    return df[column].median()

@flow
def get_started():
    data = read_csv("../../data/heart.csv")
    return get_median(data, 'age')

@flow
def get_medians():
    data = read_csv("../../data/heart.csv")
    medians = [[i, get_median(data, i)] for i in data.columns]
    return medians

print(get_started())
print(get_medians())
