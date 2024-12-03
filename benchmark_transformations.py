import time
import pandas as pd
import psutil

def benchmark_transformation(data):
    start_time = time.time()
    # Exemple de transformation : Filtrage
    transformed_data = data[data['value'] > 10]
    elapsed_time = time.time() - start_time
    memory_usage = psutil.Process().memory_info().rss / (1024 * 1024)  # En Mo
    return elapsed_time, memory_usage

if __name__ == "__main__":
    # Charger des données exemple
    data = pd.DataFrame({'value': range(1000000)})
    elapsed_time, memory_usage = benchmark_transformation(data)
    print(f"Temps d'exécution : {elapsed_time:.2f} s")
    print(f"Utilisation mémoire : {memory_usage:.2f} Mo")
