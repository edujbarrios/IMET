import json
import pandas as pd

def save_metadata_to_files(metadata_list):
    """Save metadata to CSV and JSON files with normalization."""
    df = pd.DataFrame(metadata_list)
    
    # Normalize numerical columns
    if not df.empty and 'width' in df.columns and 'height' in df.columns:
        df['width'] = df['width'] / df['width'].max()
        df['height'] = df['height'] / df['height'].max()
    
    # Save to CSV
    df.to_csv('metadata_normalized.csv', index=False)
    
    # Save to JSON
    with open('metadata_normalized.json', 'w') as json_file:
        json.dump(metadata_list, json_file, indent=4)
    
    print("Metadatos guardados en 'metadata_normalized.csv' y 'metadata_normalized.json'.")
