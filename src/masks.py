from src.logger import get_logger

logger = get_logger(__name__)


def get_mask_card_number(card_number: str) -> str:
    """
    Маскировка номера карты.
    """

    if not card_number:
        logger.error("Не передан номер карты")
        return ""

    result = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

    logger.debug(
        "Номер карты успешно замаскирован"
    )

    return result


def get_mask_account(account_number: str) -> str:
    """
    Маскировка номера счета.
    """

    if not account_number:
        logger.error("Не передан номер счета")
        return ""

    result = f"**{account_number[-4:]}"

    logger.debug(
        "Номер счета успешно замаскирован"
    )

    return result
