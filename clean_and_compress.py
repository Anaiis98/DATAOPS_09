
import pandas as pd

def clean_and_compress(input_file, output_file):
    # Charger les données
    data = pd.read_csv(input_file)
    # Exemple de nettoyage : suppression des valeurs manquantes
    cleaned_data = data.dropna()
    # Compression en Parquet
    cleaned_data.to_parquet(output_file, compression='snappy')
    print(f"Fichier compressé enregistré : {output_file}")

if __name__ == "__main__":
    # Utiliser output_data.csv comme fichier source
    clean_and_compress("output_data.csv", "compressed_file.parquet")
