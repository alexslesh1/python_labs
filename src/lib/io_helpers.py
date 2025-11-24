"""
Вспомогательные функции для работы с файлами
"""

from pathlib import Path
import json
import csv


def read_file(file_path: str, encoding: str = "utf-8") -> str:
    """
    Читает содержимое файла
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Файл не найден: {file_path}")

    with path.open("r", encoding=encoding) as f:
        return f.read()


def write_file(file_path: str, content: str, encoding: str = "utf-8") -> None:
    """
    Записывает содержимое в файл
    """
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding=encoding) as f:
        f.write(content)


def get_file_extension(file_path: str) -> str:
    """
    Возвращает расширение файла в нижнем регистре
    """
    return Path(file_path).suffix.lower()
