import pandas as pd
import plotly.express as px

# Charger les données
data = pd.read_csv("output_data.csv")

# Créer un graphique interactif
fig = px.line(data, x='x', y='y', title="Interactive Visualization")

# Sauvegarder en HTML
fig.write_html("visualization.html")

print("Graphique généré et sauvegardé sous 'visualization.html'")

