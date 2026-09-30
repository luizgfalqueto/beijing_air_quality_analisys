import pandas as pd
from pathlib import Path

dir = Path('datasets')

df_list = [pd.read_csv(file) for file in dir.glob('*.csv')]

df_consolidate = pd.concat(df_list, ignore_index=True)

df_consolidate['datetime'] = pd.to_datetime(df_consolidate[['year','month','day','hour']])

df_consolidate.to_csv('beijing_air_quality_ds.csv', index=False, encoding='utf-8')