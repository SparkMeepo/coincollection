# === Stage 8: Сортировка записей ===
# Project: CoinCollection
from typing import List, Callable


def sort_by_name(coins: List[dict], reverse: bool = False) -> List[dict]:
    """Сортирует монеты по названию, по возрастанию или убыванию."""
    return sorted(coins, key=lambda c: c['name'], reverse=reverse)


def sort_by_creation_date(coins: List[dict], reverse: bool = False) -> List[dict]:
    """Сортирует монеты по дате создания записи, по возрастанию или убыванию."""
    return sorted(coins, key=lambda c: c['created_at'], reverse=reverse)


def sort_coins(coins: List[dict], field: str, reverse: bool = False) -> List[dict]:
    """Универсальная сортировка записей монет по указанному полю.

    Поддерживает поля 'name' и 'created_at'. Для любого другого поля
    используется значение по умолчанию, чтобы не вызывать ошибку.
    """
    if field == 'name':
        key_func = lambda c: c['name']
    elif field == 'created_at':
        key_func = lambda c: c['created_at']
    else:
        key_func = lambda c: c.get(field, c['name'])
    return sorted(coins, key=key_func, reverse=reverse)


if __name__ == '__main__':
    sample = [
        {'name': 'Императорская', 'country': 'Россия', 'year': 2020, 'state': 'MS', 'created_at': '2023-05-10'},
        {'name': 'Альфа', 'country': 'Германия', 'year': 2019, 'state': 'XF', 'created_at': '2021-03-01'},
        {'name': 'Бета', 'country': 'Япония', 'year': 2022, 'state': 'AU', 'created_at': '2022-11-15'},
        {'name': 'Омега', 'country': 'США', 'year': 2018, 'state': 'VF', 'created_at': '2020-07-20'},
    ]

    print('По названию (по возрастанию):')
    for c in sort_by_name(sample):
        print(c['name'])

    print('По названию (по убыванию):')
    for c in sort_by_name(sample, reverse=True):
        print(c['name'])

    print('По дате создания (по возрастанию):')
    for c in sort_by_creation_date(sample):
        print(c['name'], c['created_at'])

    print('По дате создания (по убыванию):')
    for c in sort_by_creation_date(sample, reverse=True):
        print(c['name'], c['created_at'])

    print('Универсальная сортировка по полю year (по возрастанию):')
    for c in sort_coins(sample, field='year'):
        print(c['name'], c['year'])
