import json


def read_json(file_path):
    with open(file_path) as f:
        date = json.load(f)
    return date


def write_json(data, file_path):
    with open(file_path, "w") as f:
        json.dump(data, f)