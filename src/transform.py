import pandas as pd

def transform(df):
    df.columns = [c.strip().lower().replace("/", "_") for c in df.columns]
    df["date_time"] = pd.to_datetime(df["date_time"])
    df["hour"] = df["date_time"].dt.hour
    df["day"] = df["date_time"].dt.day
    df["month"] = df["date_time"].dt.month
    print(f"Transformed {len(df)} rows")
    return df