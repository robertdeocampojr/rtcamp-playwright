import json
from os import path
import os.path


def load_json():
    file_path = path.join(os.getcwd(), 'config/data.json')
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)

    return data
