import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("output_data.csv")
plt.plot(data['x'], data['y'])
plt.title("Example Visualization")
plt.savefig("visualization.png")

