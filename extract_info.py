import json

def extract_info_from_json(file_path, keys_to_extract):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        extracted_info = {}
        for key in keys_to_extract:
            if key in data:
                extracted_info[key] = data[key]
            else:
                extracted_info[key] = None
        
        return extracted_info

    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: File {file_path} is not a valid JSON.")
        return {}

if __name__ == "__main__":
    file_path = 'sample.json'
    keys = ['name', 'email', 'skills', 'city']  # 'city' won't be found because it's nested
    extracted_data = extract_info_from_json(file_path, keys)
    print(extracted_data)
