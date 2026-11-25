# === Stage 12: Постраничный вывод ===
# Project: CoinCollection
def paginate(coins, page, per_page):
    """Разбивает список монет на страницы."""
    start = (page - 1) * per_page
    return coins[start:start + per_page]


def validate_page_params(page, per_page):
    """Проверяет корректность параметров пагинации."""
    if page < 1:
        raise ValueError("Номер страницы должен быть не меньше 1")
    if per_page < 1:
        raise ValueError("Размер страницы должен быть не меньше 1")


def get_page_info(coins, page, per_page):
    """Возвращает содержимое страницы и метаданные о пагинации."""
    validate_page_params(page, per_page)
    total_pages = (len(coins) + per_page - 1) // per_page
    current_page = min(page, total_pages)
    page_coins = paginate(coins, current_page, per_page)
    return {
        "coins": page_coins,
        "page": current_page,
        "per_page": per_page,
        "total": len(coins),
        "total_pages": total_pages,
        "has_next": current_page < total_pages,
        "has_prev": current_page > 1,
    }
