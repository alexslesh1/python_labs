import pytest
import json
import csv
import sys
import os
from pathlib import Path

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.dirname(current_dir)
sys.path.insert(0, src_dir)

from lab05.json_csv import json_to_csv, csv_to_json


class TestJsonToCsv:
    def test_basic_conversion(self, tmp_path):
        src = tmp_path / "test.json"
        dst = tmp_path / "test.csv"
        data = [
            {"name": "Alice", "age": 22, "city": "Moscow"},
            {"name": "Bob", "age": 25, "city": "SPb"},
        ]
        src.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        json_to_csv(str(src), str(dst))
        with open(dst, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        assert len(rows) == 2
        assert set(rows[0].keys()) == {"name", "age", "city"}
        assert rows[0]["name"] == "Alice"
        assert rows[1]["name"] == "Bob"

    def test_file_not_found(self):
        with pytest.raises(FileNotFoundError):
            json_to_csv("nonexistent.json", "output.csv")

    def test_invalid_json(self, tmp_path):
        src = tmp_path / "invalid.json"
        dst = tmp_path / "output.csv"
        src.write_text("{ invalid json }", encoding="utf-8")
        with pytest.raises(ValueError):
            json_to_csv(str(src), str(dst))


class TestCsvToJson:
    def test_basic_conversion(self, tmp_path):
        src = tmp_path / "test.csv"
        dst = tmp_path / "test.json"
        csv_content = "name,age,city\nAlice,22,Moscow\nBob,25,SPb"
        src.write_text(csv_content, encoding="utf-8")
        csv_to_json(str(src), str(dst))
        with open(dst, "r", encoding="utf-8") as f:
            data = json.load(f)
        assert len(data) == 2
        assert data[0] == {"name": "Alice", "age": "22", "city": "Moscow"}
        assert data[1] == {"name": "Bob", "age": "25", "city": "SPb"}

    def test_file_not_found(self):
        with pytest.raises(FileNotFoundError):
            csv_to_json("nonexistent.csv", "output.json")

    def test_empty_csv(self, tmp_path):
        src = tmp_path / "empty.csv"
        dst = tmp_path / "output.json"
        src.write_text("", encoding="utf-8")
        with pytest.raises(ValueError):
            csv_to_json(str(src), str(dst))


class TestRoundTrip:
    def test_json_csv_json(self, tmp_path):
        original_data = [{"name": "Test", "value": 42}, {"name": "Demo", "value": 24}]
        json1 = tmp_path / "test1.json"
        csv_file = tmp_path / "test.csv"
        json2 = tmp_path / "test2.json"
        json1.write_text(
            json.dumps(original_data, ensure_ascii=False), encoding="utf-8"
        )
        json_to_csv(str(json1), str(csv_file))
        csv_to_json(str(csv_file), str(json2))
        with open(json2, "r", encoding="utf-8") as f:
            final_data = json.load(f)
        assert len(final_data) == len(original_data)
        assert final_data[0]["name"] == original_data[0]["name"]
