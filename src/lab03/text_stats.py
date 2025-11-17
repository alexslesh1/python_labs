import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lib.text import normalize, tokenize, count_freq, top_n

def analyze_text(text, top_count=5):
    """
    Анализирует текст и возвращает статистику
    """
    if not text.strip():
        raise ValueError('Нет текста :(')
    
    normalized_text = normalize(text, casefold=True, yo2e=True)
    tokens = tokenize(normalized_text)
    total_words = len(tokens)
    unique_words = len(set(tokens))
    freq = count_freq(tokens)
    top_words = top_n(freq, top_count)
    
    return {
        'total_words': total_words,
        'unique_words': unique_words,
        'top_words': top_words
    }

def main():
    text = input()
    
    result = analyze_text(text)
    
    print(f"Всего слов: {result['total_words']}")
    print(f"Уникальных слов: {result['unique_words']}")
    print("Топ-5:")
    for word, count in result['top_words']:
        print(f"{word}:{count}")

if __name__ == "__main__":
    main()