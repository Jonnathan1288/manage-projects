import json

def synchronize_and_sort_files(file1, file2):
    # Read the content of the first .arb file
    with open(file1, 'r', encoding='utf-8') as file:
        data1 = json.load(file)

    # Read the content of the second .arb file
    with open(file2, 'r', encoding='utf-8') as file:
        data2 = json.load(file)

    # Get all unique keys from both files
    keys = set(data1.keys()).union(data2.keys())

    # Synchronize the data: ensure both files have the same keys
    data1_synchronized = {key: data1.get(key, '') for key in keys}
    data2_synchronized = {key: data2.get(key, '') for key in keys}

    # Sort the keys alphabetically
    data1_sorted = {k: data1_synchronized[k] for k in sorted(data1_synchronized.keys())}
    data2_sorted = {k: data2_synchronized[k] for k in sorted(data2_synchronized.keys())}

    # Save the synchronized and sorted files
    with open(file1, 'w', encoding='utf-8') as file:
        json.dump(data1_sorted, file, ensure_ascii=False, indent=2)

    with open(file2, 'w', encoding='utf-8') as file:
        json.dump(data2_sorted, file, ensure_ascii=False, indent=2)

# Synchronize and sort the files app_en.arb and app_es.arb
synchronize_and_sort_files('app_en.arb', 'app_es.arb')
