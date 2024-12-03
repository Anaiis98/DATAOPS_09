import matplotlib.pyplot as plt
import pandas as pd
import os

print("Current working directory:", os.getcwd())
try:
    data = pd.read_csv("output_data.csv")
    print("Data loaded successfully:\n", data.head())
    plt.plot(data['x'], data['y'])
    plt.title("Example Visualization")
    plt.savefig("visualization.png")
    print("Image saved successfully as 'visualization.png'")
except Exception as e:
    print("An error occurred:", str(e))

