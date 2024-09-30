#!/usr/bin/python3
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file.
    
    Parameters:
        data (dict): The data to be serialized.
        filename (str): The name of the file to save the serialized data.
    """
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4) 

def load_and_deserialize(filename):
    """
    Load and deserialize JSON data from a file, recreating a Python dictionary.

    Parameters:
        filename (str): The name of the file to load and deserialize.

    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data

if __name__ == "__main__":
    # Sample data to be serialized
    data_to_serialize = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }

    # Serialize the data to JSON and save it to a file
    serialize_and_save_to_file(data_to_serialize, 'data.json')

    # Output: The data has been serialized and saved to 'data.json'
    print("Data serialized and saved to 'data.json'.")

    # Load and deserialize data from 'data.json'
    deserialized_data = load_and_deserialize('data.json')

    # Output: The deserialized data
    print("Deserialized Data:")
    print(deserialized_data)
    