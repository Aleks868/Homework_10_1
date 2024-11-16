import json


def transaction_amount(file_path: str) -> list:
    """Функция принимает путь к JSON файлу и возвращает список словарей с транзакциями"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            repos = json.load(file)
        if isinstance(repos, list):
            return repos
        else:
            return []
    except Exception as e:
        print(f"Ошибка {e}")
        return []
