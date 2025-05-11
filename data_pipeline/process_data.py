# Code to process raw federal data
import pandas as pd

def clean_data(file_path):
    df = pd.read_csv(file_path)
    df.dropna(inplace=True)
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
    return df
