# === Stage 6: Связи между сущностями ===
# Project: CoinCollection
from collections import defaultdict


class Coin:
    def __init__(self, name, country, year, condition):
        self.name = name
        self.country = country
        self.year = year
        self.condition = condition


class Grade:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class CoinCollection:
    def __init__(self):
        self._grades_by_coin = defaultdict(list)
        self._coins = []

    def add_coin(self, coin):
        self._coins.append(coin)
        self._grades_by_coin[coin].clear()

    def add_grade(self, coin, grade):
        self._grades_by_coin[coin].append(grade)

    def get_all_grades(self, coin):
        grades = self._grades_by_coin[coin]
        self._check_integrity(coin, grades)
        return list(grades)

    def _check_integrity(self, coin, grades):
        if coin not in self._coins:
            raise KeyError(f"Монета '{coin.name}' не найдена в коллекции")
        if grades is None:
            raise ValueError(f"У монеты '{coin.name}' отсутствует оценка")
        if len(grades) == 0:
            raise ValueError(f"У монеты '{coin.name}' нет оценок")
        for grade in grades:
            if not isinstance(grade, Grade):
                raise TypeError(f"Оценка '{grade}' имеет неверный тип")
            if grade.value is None:
                raise ValueError(f"Оценка '{grade.name}' имеет пустое значение")
