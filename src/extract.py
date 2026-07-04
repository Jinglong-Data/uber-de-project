import pandas as pd

def extract():
    url = "https://raw.githubusercontent.com/fivethirtyeight/uber-tlc-foil-response/master/uber-trip-data/uber-raw-data-apr14.csv"
    df = pd.read_csv(url)
    print(f"Extracted {len(df)} rows")
    return df

if __name__ == "__main__":
    df = extract()
    print(df.head())