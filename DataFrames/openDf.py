import pandas as pd
import plotly.express as px

store = pd.HDFStore('store.h5')

df = store['df']


print(df)