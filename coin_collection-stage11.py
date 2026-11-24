# === Stage 11: Группировка ===
# Project: CoinCollection
from collections import Counter

class Coin:
    def __init__(self, name, country, year, condition):
        self.name = name
        self.country = country
        self.year = year
        self.condition = condition

    def __repr__(self):
        return f"Coin(name={self.name!r}, country={self.country!r}, year={self.year!r}, condition={self.condition!r})"


def group_by_country(coins):
    grouped = {}
    for coin in coins:
        grouped.setdefault(coin.country, []).append(coin)
    return grouped


def count_by_country(coins):
    counts = Counter(coin.country for coin in coins)
    return dict(counts)


def group_and_count(coins):
    grouped = group_by_country(coins)
    counts = {country: len(group) for country, group in grouped.items()}
    return grouped, counts


if __name__ == "__main__":
    collection = [
        Coin("10 копеек", "СССР", 1961, "ХС"),
        Coin("50 копеек", "СССР", 1961, "С"),
        Coin("1 рубль", "СССР", 1961, "С"),
        Coin("10 центов", "США", 1964, "С"),
        Coin("25 центов", "США", 1964, "С"),
        Coin("1 фунт", "Великобритания", 1970, "С"),
    ]

    grouped, counts = group_and_count(collection)

    print("Группировка по странам:")
    for country, group in grouped.items():
        print(f"  {country}: {len(group)} монет")

    print("Страны и их количество:")
    for country, count in counts.items():
        print(f"  {country}: {count}")
