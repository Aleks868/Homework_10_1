import json
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s: %(filename)s: %(levelname)s: %(message)s",
    filename="../logs/utils.log",
    filemode="w",
                    )

logger = logging.getLogger("utils")


def transaction_amount(file_path: str) -> list:
    """Функция принимает путь к JSON файлу и возвращает список словарей с транзакциями"""
    logger.info("Starts transaction_amount")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            repos = json.load(file)
        if isinstance(repos, list):
            logger.info("Transactions list ready")
            return repos
        else:
            return []
    except Exception as e:
        logger.error(f"Ошибка {e}")
        print(f"Ошибка {e}")
        return []
