# === Stage 3: Хранилище в памяти ===
# Project: CoinCollection
import threading
from typing import Dict, List, Optional


class Coin:
    __slots__ = ("id", "name", "country", "year", "condition")

    def __init__(self, name: str, country: str, year: int, condition: str) -> None:
        self.name = name
        self.country = country
        self.year = year
        self.condition = condition

    def __repr__(self) -> str:
        return f"Coin(name={self.name!r}, country={self.country!r}, year={self.year}, condition={self.condition!r})"


class CoinStore:
    _store_lock = threading.Lock()
    _counter = 0

    def __init__(self) -> None:
        self._coins: Dict[int, Coin] = {}

    def add_coin(self, coin: Coin) -> int:
        with self._store_lock:
            coin.id = self._counter
            self._counter += 1
            self._coins[coin.id] = coin
            return coin.id

    def get_coin(self, coin_id: int) -> Optional[Coin]:
        with self._store_lock:
            return self._coins.get(coin_id)

    def list_coins(self) -> List[Coin]:
        with self._store_lock:
            return list(self._coins.values())

    def delete_coin(self, coin_id: int) -> bool:
        with self._store_lock:
            return self._coins.pop(coin_id, None) is not None


def main() -> None:
    store = CoinStore()

    c1 = Coin("Liberation", "USA", 1935, "Uncirculated")
    c2 = Coin("Eagle", "USA", 2009, "Worn")

    id1 = store.add_coin(c1)
    id2 = store.add_coin(c2)

    print(f"Added coin 1 with id={id1}")
    print(f"Added coin 2 with id={id2}")

    retrieved = store.get_coin(id1)
    print(f"Retrieved coin: {retrieved}")

    print("Current collection:")
    for coin in store.list_coins():
        print(f"  id={coin.id}, name={coin.name}, country={coin.country}, "
              f"year={coin.year}, condition={coin.condition}")

    print(f"Coin with id={id2}: {store.get_coin(id2)}")


if __name__ == "__main__":
    main()
