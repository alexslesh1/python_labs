from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, date


@dataclass
class Student:
    fio: str
    birthdate: str   # формат YYYY-MM-DD
    group: str
    gpa: float       # 0..5

    def __post_init__(self):
        # Проверка формата даты
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Invalid birthdate format: {self.birthdate}. Expected YYYY-MM-DD")

        # Проверка диапазона GPA
        if not (0 <= self.gpa <= 5):
            raise ValueError("GPA must be between 0 and 5")

    def age(self) -> int:
        """Возвращает количество полных лет."""
        bdate = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        years = today.year - bdate.year
        if (today.month, today.day) < (bdate.month, bdate.day):
            years -= 1
        return years

    def to_dict(self) -> dict:
        """Сериализация в словарь."""
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Student":
        """Создание объекта из словаря."""
        return cls(
            fio=data["fio"],
            birthdate=data["birthdate"],
            group=data["group"],
            gpa=float(data["gpa"]),
        )

    def __str__(self):
        return f"{self.fio} ({self.group}), GPA={self.gpa}, age={self.age()} y/o"