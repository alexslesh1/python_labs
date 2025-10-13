# Лабораторная работа №3

## Архитектура проекта
```
📦 PYTHON_LABS
┣ 📂 misc
┣ 📂 src
┃  ┣ 📂 lab01
┃  ┣ 📂 lab02
┃  ┗ 📂 lab03
┃     ┣ 📜 README.md                    # Отчет по по функциям из ЛР3
┃     ┗ 📜 text_stats.py                # Основная программа анализа текста
┣ 📂 lib                                     
┃  ┣ 📜 text.py                         # Библиотека функций для работы с текстом
┃  ┗ 📂 __pycache__
┣ 📂 images
┃  ┗ 📂 lab03
┃     ┗ 📜 screenshot1.png              # Скриншот работы программы
┗ 📜 README.md                          # Общий отчет по ЛР3
```

## Задание A 

### Функция №1

**Описание:** Функция выполняет нормализацию текста - приводит его к стандартному виду для последующей обработки.

**Исходный код функции:**
```
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    result = text
    
    if casefold:
        result = result.casefold()    
    if yo2e:
        result = result.replace('ё', 'е').replace('Ё', 'е')
    
    for char in ['\t', '\r', '\n']:
        result = result.replace(char, ' ')
    
    result = re.sub(r'\s+', ' ', result).strip()
    return result
```

### Функция №2

**Описание:** Функция выполняет разбиение текста на слова (токены) используя регулярные выражения.

**Исходный код функции:** 
```
def tokenize(text: str) -> List[str]:
    pattern = r'\w+(?:-\w+)*'
    tokens = re.findall(pattern, text)
    return tokens
```

### Функция №3

**Описание:** Функция выполняет подсчет частоты встречаемости слов в списке токенов.

**Исходный код функции:** 
```
def count_freq(tokens: List[str]) -> Dict[str, int]:
    frequency_dict = {}
    for token in tokens:
        frequency_dict[token] = frequency_dict.get(token, 0) + 1
    return frequency_dict
```

### Функция №4

**Описание:** Функция возвращает N самых частых слов из словаря частот с сортировкой.

**Исходный код функции:** 
```
def top_n(freq: Dict[str, int], n: int = 5) -> List[Tuple[str, int]]:
    items = list(freq.items())
    sorted_items = sorted(items, key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]
```

**Добавьте приведенные ниже тест-кейсы в файл `text.py` для проведения проверки.**
```
print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка")) 
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))

print(tokenize("привет мир" ))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год" ))
print(tokenize("emoji 😀 не слово" ))

print(count_freq(["a","b","a","c","b","a"]))
print(count_freq(["bb", "aa", "bb", "aa", "cc"]))

freq1 = {"a": 3, "b": 2, "c": 1}
print(top_n(freq1, 2))
freq2 = {"bb": 2, "aa": 2, "cc": 1}
print(top_n(freq2, 2))
```

**Пример использования:** 
![](misc/img/lab03/text_py_photo.png)

## Задание B

**Описание:** Программа для анализа текстовой статистики. Читает одну строку текста от пользователя, обрабатывает её и выводит:
* Общее количество слов
* Количество уникальных слов
* Топ-5 самых частых слов с их частотами 

**Исходный код**
```
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lib.text import normalize, tokenize, count_freq, top_n

def main():
    text = input()
    
    if not text.strip():
        raise ValueError('Нет текста :(')
    
    normalized_text = normalize(text, casefold=True, yo2e=True)
    tokens = tokenize(normalized_text)
    total_words = len(tokens)
    unique_words = len(set(tokens))
    freq = count_freq(tokens)
    top_words = top_n(freq, 5)
    
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    for word, count in top_words:
        print(f"{word}:{count}")

if __name__ == "__main__":
    main()
```

**Пример использования:** 
![](misc/img/lab03/text_stats_py_photo.png)

## Вывод 
В лабораторной работе №3 успешно разработана система анализа текстовой статистики. Реализованы 4 основные функции: normalize() для нормализации текста, tokenize() для разбивки на слова, count_freq() для подсчета частот и top_n() для вывода наиболее частых слов. Создана программа text_stats.py, которая читает текст из stdin и выводит статистику: общее количество слов, количество уникальных слов и топ-5 самых частых слов. Все функции протестированы и готовы к переиспользованию в следующих лабораторных работах.