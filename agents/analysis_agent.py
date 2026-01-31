from tools.data_loader import load_csv
from tools.data_cleaner import clean_data
from tools.eda_tool import eda_summary

def run_analysis(file_path):
    df = load_csv(file_path)
    df = clean_data(df)
    eda = eda_summary(df)
    return df, eda
