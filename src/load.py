from sqlalchemy import create_engine

def load(df):
    engine = create_engine("sqlite:///uber.db")
    df.to_sql("uber_trips", engine, if_exists="replace", index=False)
    print("Data loaded to uber.db")