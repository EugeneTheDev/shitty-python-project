"""
Проверка правильности введенных данных
"""


def validate_number(text):
    """
    Проверка на число
    """

    if not text:
        raise ValueError
    res = int(text)
    if res < 0:
        raise ValueError
    return res


def validate_text(text):
    """
    Проверка на корректную строку
    """

    if "," in text:
        raise ValueError
    return text.strip()
