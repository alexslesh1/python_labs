from pathlib import Path
import json
import csv
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../lib'))
from io_helpers import read_file, write_file, get_file_extension

def validate_extension(path: str, expected_ext: str) -> None:

    actual_ext = get_file_extension(path)
    if actual_ext != expected_ext.lower():
        raise ValueError(f"Неверный формат: {path}. Ожидается {expected_ext}")

def json_to_csv(json_path: str, csv_path: str) -> None:

    validate_extension(json_path, '.json')
    validate_extension(csv_path, '.csv')
    json_content = read_file(json_path)
    data = json.loads(json_content)
    
    if not data:
        raise ValueError("JSON файл пуст")
    
    fieldnames = list(data[0].keys())
    csv_content = []   
    csv_content.append(','.join(fieldnames))

    for item in data:
        row = [str(item.get(field, '')) for field in fieldnames]
        csv_content.append(','.join(row))
    write_file(csv_path, '\n'.join(csv_content))
    print(f"JSON -> CSV завершено: {csv_path}")


def csv_to_json(csv_path: str, json_path: str) -> None:
    validate_extension(csv_path, '.csv')
    validate_extension(json_path, '.json')
    csv_content = read_file(csv_path)
    from io import StringIO
    csv_file = StringIO(csv_content)
    data = list(csv.DictReader(csv_file))
    
    if not data:
        raise ValueError("CSV файл пуст")
    json_content = json.dumps(data, indent=2, ensure_ascii=False)
    write_file(json_path, json_content)
    
    print(f"CSV -> JSON завершено: {json_path}")