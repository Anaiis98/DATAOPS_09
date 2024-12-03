import pandas as pd

df = pd.read_csv("input_data.csv")
df.to_csv("output_data.csv", index=False)
