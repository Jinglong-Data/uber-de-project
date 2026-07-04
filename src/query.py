import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///uber.db")
df = pd.read_sql("SELECT * FROM uber_trips LIMIT 10", engine)
print(df)

# Some fun analysis
print("\nTrips per hour:")
print(pd.read_sql("SELECT hour, COUNT(*) as trips FROM uber_trips GROUP BY hour ORDER BY hour", engine))
