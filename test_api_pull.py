# test_pull.py
import os, pandas as pd
from fredapi import Fred

fred = Fred(api_key=os.getenv("FRED_API_KEY"))
df = fred.get_series("UNRATE", observation_start="2020-01-01").to_frame("Unrate")
print(df.tail())

