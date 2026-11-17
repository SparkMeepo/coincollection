# === Stage 7: Фильтрация записей ===
# Project: CoinCollection
def filter_coins(coins, country=None, year_range=None):
    """Фильтрует монеты по стране и/или диапазону лет выпуска."""
    result = []
    for coin in coins:
        if country is not None and coin.get("country") != country:
            continue
        if year_range is not None:
            year = coin.get("year")
            if year is None or not (year_range[0] <= year <= year_range[1]):
                continue
        result.append(coin)
    return result


def filter_by_country(coins, country):
    """Возвращает все монеты, чья страна совпадает с переданным значением."""
    return [coin for coin in coins if coin.get("country") == country]


def filter_by_year_range(coins, start_year, end_year):
    """Возвращает монеты с годом выпуска в диапазоне от start_year до end_year включительно."""
    return [
        coin for coin in coins
        if coin.get("year") is not None
        and start_year <= coin["year"] <= end_year
    ]


def filter_by_country_and_year_range(coins, country, start_year, end_year):
    """Комбинирует фильтрацию по стране и диапазону лет."""
    return [
        coin for coin in coins
        if coin.get("country") == country
        and coin.get("year") is not None
        and start_year <= coin["year"] <= end_year
    ]


if __name__ == "__main__":
    sample = [
        {"name": "Ruble", "country": "Russia", "year": 1997},
        {"name": "Dinar", "country": "UAE", "year": 2015},
        {"name": "Yen", "country": "Japan", "year": 2000},
        {"name": "Euro", "country": "Germany", "year": 2002},
    ]
    print(filter_by_country(sample, "Japan"))
    print(filter_by_year_range(sample, 1990, 2010))
    print(filter_by_country_and_year_range(sample, "UAE", 2010, 2020))
