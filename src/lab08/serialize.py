import json
from .models import Student


def students_to_json(students, path):
    """Сохраняет список студентов в JSON-файл."""
    data = [s.to_dict() for s in students]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def students_from_json(path):
    """Загружает список студентов из JSON-файла."""
    with open(path, "r", encoding="utf-8") as f:
        raw = json.load(f)
    return [Student.from_dict(item) for item in raw]