from dagster import asset
import pandas as pd

@asset
def df_heart():
    df = pd.read_csv('../../data/heart.csv')
    return df

@asset
def df_saturation():
    df = pd.read_csv('../../data/o2Saturation.csv')
    return df

@asset
def df_full(df_heart, df_saturation):
    df = df_heart.merge(df_saturation)
    return df

