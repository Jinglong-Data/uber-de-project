from extract import extract
from transform import transform
from load import load

df = extract()
df = transform(df)
load(df)
print("Pipeline complete!")