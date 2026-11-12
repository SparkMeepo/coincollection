# === Stage 4: Удаление и восстановление ===
# Project: CoinCollection
import datetime


class SoftDeleteMixin:
    """Добавляет логическое удаление с возможностью восстановления."""

    deleted_at = None
    is_deleted = False

    def soft_delete(self):
        self.deleted_at = datetime.datetime.now()
        self.is_deleted = True

    def restore(self):
        self.deleted_at = None
        self.is_deleted = False


class Coin(SoftDeleteMixin):
    def __init__(self, name, country, year, condition):
        self.name = name
        self.country = country
        self.year = year
        self.condition = condition

    def soft_delete(self):
        super().soft_delete()

    def restore(self):
        super().restore()

    def __repr__(self):
        status = "удалена" if self.is_deleted else "активна"
        return f"Coin(name={self.name!r}, country={self.country!r}, year={self.year}, condition={self.condition!r}, status={status})"


def remove_coin(collection, coin):
    collection.remove(coin)
    coin.soft_delete()


def find_deleted_coins(collection):
    return [coin for coin in collection if coin.is_deleted]


def restore_deleted_coins(collection):
    for coin in find_deleted_coins(collection):
        coin.restore()


if __name__ == "__main__":
    collection = []
    coin = Coin("Lira", "Турция", 1923, "Бюллетень")
    collection.append(coin)
    print(coin)
    remove_coin(collection, coin)
    print(coin)
    restore_deleted_coins(collection)
    print(coin)
