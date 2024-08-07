import json

def sort_arb_keys(file):
    # Read the content of the .arb file
    with open(file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # Sort the keys alphabetically
    sorted_data = {k: data[k] for k in sorted(data.keys())}
    
    # Save the sorted content in the same file
    with open(file, 'w', encoding='utf-8') as file:
        json.dump(sorted_data, file, ensure_ascii=False, indent=2)

# Sort the app_en.arb file
sort_arb_keys('app_en.arb')
