import argparse
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "lab03"))

from text_stats import normalize, tokenize, count_freq, top_n


def validate_txt_file(filename):
    """Проверяет, что файл имеет расширение .txt"""
    if not filename.lower().endswith(".txt"):
        raise ValueError(f"Файл должен иметь расширение .txt: {filename}")


def cat_command(input_file, number_lines=False):
    try:
        validate_txt_file(input_file)

        with open(input_file, "r", encoding="utf-8") as file:
            lines = file.readlines()

        for i, line in enumerate(lines, 1):
            if number_lines:
                print(f"{i:6d}\t{line.rstrip()}")
            else:
                print(line.rstrip())

    except FileNotFoundError:
        raise FileNotFoundError(f"Файл не найден: {input_file}")
    except Exception as e:
        raise Exception(f"Ошибка при чтении файла: {e}")


def stats_command(input_file, top_count=5):
    try:
        validate_txt_file(input_file)

        with open(input_file, "r", encoding="utf-8") as file:
            text = file.read()

        if not text.strip():
            raise ValueError("Файл пуст")

        # Используем функции из lab03
        normalized_text = normalize(text, casefold=True, yo2e=True)
        tokens = tokenize(normalized_text)
        total_words = len(tokens)
        unique_words = len(set(tokens))
        freq = count_freq(tokens)
        top_words = top_n(freq, top_count)

        print(f"Анализ файла: {input_file}")
        print(f"Всего слов: {total_words}")
        print(f"Уникальных слов: {unique_words}")
        print(f"Топ-{top_count} самых частых слов:")
        for word, count in top_words:
            print(f"  {word}: {count}")

    except FileNotFoundError:
        raise FileNotFoundError(f"Файл не найден: {input_file}")
    except Exception as e:
        raise Exception(f"Ошибка при анализе текста: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="CLI-утилита для работы с текстовыми файлами",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", help="Доступные команды")

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Входной файл")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Анализ частот слов в тексте")
    stats_parser.add_argument("--input", required=True, help="Входной текстовый файл")
    stats_parser.add_argument(
        "--top", type=int, default=5, help="Количество топ-слов (по умолчанию: 5)"
    )

    args = parser.parse_args()

    try:
        if args.command == "cat":
            cat_command(args.input, args.n)
        elif args.command == "stats":
            stats_command(args.input, args.top)
        else:
            parser.print_help()

    except FileNotFoundError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Неожиданная ошибка: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
