# === Stage 13: Быстрые фильтры ===
# Project: CoinCollection
from datetime import datetime, date

DATE_FORMAT = "%Y-%m-%d"
TODAY = date.today()
WEEK_START = (TODAY - timedelta(days=TODAY.weekday())).date()


def _parse(coin):
    try:
        issue_date = datetime.strptime(coin["issue_date"], DATE_FORMAT).date()
    except (KeyError, TypeError, ValueError):
        return None
    if isinstance(issue_date, date) and issue_date <= TODAY:
        return issue_date
    return None


def is_today(coin):
    parsed = _parse(coin)
    return parsed is not None and parsed == TODAY


def is_this_week(coin):
    parsed = _parse(coin)
    return parsed is not None and WEEK_START <= parsed <= TODAY


def is_expired(coin):
    parsed = _parse(coin)
    return parsed is not None and parsed < WEEK_START


def filter_by_date(coin, mode):
    if mode == "today":
        return is_today(coin)
    if mode == "this_week":
        return is_this_week(coin)
    if mode == "expired":
        return is_expired(coin)
    raise ValueError(f"Неизвестный режим фильтрации: {mode!r}")


def get_date_filters(coins, mode):
    return [coin for coin in coins if filter_by_date(coin, mode)]


def add_issue_date(coin, issue_date):
    coin["issue_date"] = issue_date


def remove_issue_date(coin):
    coin.pop("issue_date", None)
