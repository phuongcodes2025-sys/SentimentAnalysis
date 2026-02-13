import json


def load_dataset(file: str) -> tuple[list[str], list[str]]:
    with open(file,'r') as f:
        doc = json.load(f)
        return doc['texts'],doc['labels']