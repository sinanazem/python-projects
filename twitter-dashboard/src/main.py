import os
import json
from pathlib import Path


def integrate_and_deduplicate_json(folder_path, output_file):
    all_data = []
    
    # Iterate over all files in the directory
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Make sure to process only JSON files
        if filename.endswith('.json'):
            with open(file_path, 'r', encoding='utf-8') as file:
                try:
                    data = json.load(file)
                    
                    # Ensure the loaded data is a list of dictionaries
                    if isinstance(data, list):
                        all_data.extend(data)
                    else:
                        print(f"Warning: {filename} does not contain a list.")
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON from {filename}: {e}")

    # Removing duplicates - Assumes that data items are dictionaries
    # Convert list of dictionaries to a list of frozensets (or tuples for hashable content)
    unique_data = [dict(s) for s in set(frozenset(d.items()) for d in all_data)]

    # Write the deduplicated data to the output JSON file
    with open(output_file, 'w', encoding='utf-8') as output:
        json.dump(unique_data, output, ensure_ascii=False, indent=4)

# Example usage
integrate_and_deduplicate_json(Path(".").resolve() / "data", Path(".").resolve() / 'integrated_output.json')
