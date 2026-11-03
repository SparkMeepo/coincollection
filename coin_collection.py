# === Stage 1: Каркас модуля ===
# Project: CoinCollection
from dataclasses import dataclass, field
from typing import List, Optional
from datetime import date


@dataclass
class Coin:
    name: str
    country: str
    year: int
    condition: str = "uncirculated"
    grade: Optional[float] = None


def sample_coins() -> List[Coin]:
    return [
        Coin("Liberty Head", "USA", 1907, "worn", 75.0),
        Coin("Krugerrand", "South Africa", 1985, "uncirculated", 98.0),
        Coin("Maple Leaf", "Canada", 1990, "mint", 99.9),
    ]


def main() -> None:
    coins = sample_coins()
    print("CoinCollection — коллекция монет")
    print(f"Демо-записей: {len(coins)}")
    for coin in coins:
        print(f"  {coin.name} ({coin.country}, {coin.year}, {coin.condition}, оценка {coin.grade})")


if __name__ == "__main__":
    main()
