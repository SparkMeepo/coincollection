# === Stage 5: Связанная сущность ===
# Project: CoinCollection
from typing import Dict, List, Optional

Grades = Dict[str, float]

GRADES = {
    "UNC": 1.0,
    "AU": 0.8,
    "XF": 0.5,
    "VF": 0.3,
    "F": 0.15,
    "VG": 0.08,
    "POOR": 0.04,
}

CoinId = str
GradeId = str
CoinGrades = Dict[CoinId, List[GradeId]]


class CoinGradesStore:
    def __init__(self) -> None:
        self._grades: CoinGrades = {}
        self._coins: CoinGrades = {}

    def add_grade(self, coin_id: CoinId, grade: GradeId) -> GradeId:
        if grade not in GRADES:
            raise ValueError(grade)
        self._grades.setdefault(coin_id, []).append(grade)
        return grade

    def get_grade(self, coin_id: CoinId, grade: GradeId) -> Optional[GradeId]:
        return grade in self._grades.get(coin_id, [])

    def get_average(self, coin_id: CoinId) -> Optional[float]:
        grades = self._grades.get(coin_id, [])
        if not grades:
            return None
        values = [GRADES[g] for g in grades]
        return sum(values) / len(values)

    def list_grades(self, coin_id: CoinId) -> List[GradeId]:
        return list(self._grades.get(coin_id, []))

    def set_coin(self, coin_id: CoinId) -> None:
        self._coins[coin_id] = True

    def has_coin(self, coin_id: CoinId) -> bool:
        return coin_id in self._coins

    def list_coins(self) -> List[CoinId]:
        return list(self._coins.keys())

    def remove_coin(self, coin_id: CoinId) -> None:
        self._grades.pop(coin_id, None)
        self._coins.pop(coin_id, None)
