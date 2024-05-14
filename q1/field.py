import numpy as np
from drone import Drone


class Field:
    _tc = 0.0
    _contact = False
    _contactCount = 0

    def __init__(
        self,
        A: int,
        B: int,
        V: int,
        r: int,
        limit: int,
        res: int,
        progress: bool = False,
    ):
        self._n1 = Drone(A, B, V)
        self._n2 = Drone(A, B, V)
        self._limit = limit
        self._r = r
        self._res = res
        self._progress = progress

    def _contactJudge(self):
        distance = np.linalg.norm(self._n1.drone - self._n2.drone)
        return distance < self._r

    def _add_tc(self):
        if self._contactJudge():
            if self._contact is False:
                self._contactCount += 1
            self._contact = True
        else:
            self._contact = False
            self._tc += 1 / self._res

    def main(self):
        for i in range(self._limit):
            t = i / self._res
            self._n1.advanceTime(t)
            self._n2.advanceTime(t)
            self._add_tc()

            if ((i / self._limit * 100) % 5 == 0) and self._progress:
                print("progress: ", i / self._limit * 100, "%")

        return self._tc / self._contactCount
