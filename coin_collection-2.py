# === Stage 2: Проверка полей ===
# Project: CoinCollection
import re


def normalize_country(value):
    if value is None:
        return ""
    cleaned = re.sub(r"\s+", " ", str(value)).strip()
    cleaned = re.sub(r"[^\w\s.-]", "", cleaned, flags=re.UNICODE)
    return cleaned


def normalize_year(value):
    if value is None:
        return None
    digits = re.sub(r"\D", "", str(value))
    if not digits:
        return None
    year = int(digits)
    if not (1 <= year <= 9999):
        return None
    return year


def normalize_condition(value):
    if value is None:
        return ""
    cleaned = str(value).strip().lower()
    return cleaned


def normalize_name(value):
    if value is None:
        return ""
    cleaned = str(value).strip()
    return cleaned


def validate_name(value):
    if value is None:
        return "", "Название монеты не может быть пустым."
    name = normalize_name(value)
    if not name:
        return "", "Название монеты не может быть пустым."
    if len(name) > 100:
        return "", "Название монеты слишком длинное."
    return name, None


def validate_country(value):
    if value is None:
        return "", "Страна не может быть пустой."
    country = normalize_country(value)
    if not country:
        return "", "Страна не может быть пустой."
    if len(country) > 100:
        return "", "Страна слишком длинная."
    return country, None


def validate_year(value):
    if value is None:
        return None, "Год не может быть пустым."
    year = normalize_year(value)
    if year is None:
        return None, "Год должен быть числом от 1 до 9999."
    return year, None


def validate_condition(value):
    if value is None:
        return "", "Состояние не может быть пустым."
    condition = normalize_condition(value)
    if not condition:
        return "", "Состояние не может быть пустым."
    if len(condition) > 100:
        return "", "Состояние слишком длинное."
    return condition, None
