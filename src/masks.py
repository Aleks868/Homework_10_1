import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s: %(filename)s: %(levelname)s: %(message)s",
    filename="../logs/mask.log",
    filemode="w",
)

logger = logging.getLogger("mask")


def get_mask_card_number(user_card_number: str) -> str:
    """Функция, скрывающая номер карты"""
    logger.info(f"start masked_card_num {user_card_number}")
    result = f"{user_card_number[:4]} {user_card_number[4:6]}** **** {user_card_number[12:]}"
    logger.info(f"mask {result}")
    return result


def get_mask_account(user_account_number: str) -> str:
    """Фкнуция, скрывающая номер счета"""
    logger.info(f"start get_mask_account {user_account_number}")
    result = f"*{user_account_number[-4:]}"
    logger.info(f"mask {result}")
    return result
