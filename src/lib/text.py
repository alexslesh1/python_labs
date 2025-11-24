import re
from typing import Dict, List, Tuple
from collections import Counter


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    result = text

    if casefold:
        result = result.casefold()
    if yo2e:
        result = result.replace("ё", "е").replace("Ё", "е")

    for char in ["\t", "\r", "\n"]:
        result = result.replace(char, " ")

    result = re.sub(r"\s+", " ", result).strip()
    return result


def tokenize(text: str) -> List[str]:
    pattern = r"\w+(?:-\w+)*"
    tokens = re.findall(pattern, text)
    return tokens


def count_freq(tokens: List[str]) -> Dict[str, int]:
    return Counter(tokens)


def top_n(freq: Dict[str, int], n: int = 5) -> List[Tuple[str, int]]:
    items = list(freq.items())
    sorted_items = sorted(items, key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]


if __name__ == "__main__":
    test_text = "Привет, мир! Привет!!! Тест-тест проверка."
    print("Исходный текст:", test_text)

    norm_text = normalize(test_text)
    print("Нормализованный:", norm_text)

    tokens = tokenize(norm_text)
    print("Токены:", tokens)

    freq = count_freq(tokens)
    print("Частоты:", freq)

    top_3 = top_n(freq, 3)
    print("Топ-3:", top_3)
