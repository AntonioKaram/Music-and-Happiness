import pandas as pd

store = pd.HDFStore('store.h5')

df = store['df']

print(df)

