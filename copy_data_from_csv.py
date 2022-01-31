import pandas as pd
from sqlalchemy import create_engine


df = pd.read_csv("dataset/flavors.csv")
df.columns = [c.lower() for c in df.columns]
engine = create_engine("postgresql://postgres:postgres@localhost:5432/postgres")
df.to_sql(name="flavors", schema="std", con=engine, if_exists="replace", index=False)
