from json_csv import json_to_csv, csv_to_json
from csv_xlsx import csv_to_xlsx, xlsx_to_csv
import os

def validate_conversion(input_path, output_path):
    if os.path.abspath(input_path) == os.path.abspath(output_path):
        raise ValueError("❌ Нельзя конвертировать файл в самого себя!")
    
    input_ext = os.path.splitext(input_path)[1].lower()
    output_ext = os.path.splitext(output_path)[1].lower()
    
    if input_ext == output_ext:
        raise ValueError(f"❌ Нельзя конвертировать {input_ext} в {output_ext} - одинаковые форматы!")
def main():
    print("Конвертер файлов :)")
    print("1. JSON → CSV")
    print("2. CSV → JSON") 
    print("3. CSV → XLSX")
    print("4. XLSX → CSV")
    
    choice = input("Выберите действие (1-4): ").strip()
    
    base_path = 'src/data/samples/'
    out_path = 'src/data/out/'
    
    try:
        if choice == '1':
            input_file = base_path + 'people.json'
            output_file = out_path + 'people.csv'
            validate_conversion(input_file, output_file)
            json_to_csv(input_file, output_file)
            
        elif choice == '2':
            input_file = base_path + 'people.csv'
            output_file = out_path + 'people.json'
            validate_conversion(input_file, output_file)
            csv_to_json(input_file, output_file)
            
        elif choice == '3':
            input_file = base_path + 'cities.csv'
            output_file = out_path + 'cities.xlsx'
            validate_conversion(input_file, output_file)
            csv_to_xlsx(input_file, output_file)
            
        elif choice == '4':
            input_file = base_path + 'cities.xlsx'
            output_file = out_path + 'cities.csv'
            validate_conversion(input_file, output_file)
            xlsx_to_csv(input_file, output_file)
            
        else:
            print("❌ Неверный выбор! Введите цифру от 1 до 4")
            
    except (FileNotFoundError, ValueError) as e:
        print(f"❌ Ошибка: {e} :()")

if __name__ == "__main__":
    main()