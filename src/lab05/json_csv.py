import json
import csv
import os

def validate_extension(path, ext):
    if not path.lower().endswith(ext.lower()):
        raise ValueError(f"Неверный формат: {path}. Ожидается {ext}")

def json_to_csv(json_path, csv_path):
    validate_extension(json_path, '.json')
    validate_extension(csv_path, '.csv')
    if not os.path.exists(json_path): raise FileNotFoundError(f"JSON не найден: {json_path}")
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        if not data: raise ValueError("JSON файл пуст")
    
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=list(data[0].keys()))
        writer.writeheader()
        writer.writerows(data)
    
    print(f"JSON -> CSV завершено: {csv_path}")

def csv_to_json(csv_path, json_path):
    validate_extension(csv_path, '.csv')
    validate_extension(json_path, '.json')
    if not os.path.exists(csv_path): raise FileNotFoundError(f"CSV не найден: {csv_path}")
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        data = list(csv.DictReader(f))
        if not data: raise ValueError("CSV файл пуст")
    
    os.makedirs(os.path.dirname(json_path), exist_ok=True)
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"CSV -> JSON завершено: {json_path}")