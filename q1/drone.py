import numpy as np
import numpy.typing as npt


class Drone:
    _startTime = 0.0

    def __init__(self, a: int, b: int, v: int):
        self._A = a
        self._B = b
        self._s = np.random.rand(2) * [a, b]
        self._d = np.random.rand(2) * [a, b]
        self._drone = self._s
        self._driveVelocity = v

    @property
    def drone(self):
        return self._drone

    @property
    def s(self):
        return self._s

    @property
    def d(self):
        return self._d

    @property
    def driveDistance(self):
        return np.linalg.norm(self._s - self._d)

    @property
    def driveTime(self):
        return self.driveDistance / self._driveVelocity

    @property
    def sdAngle(self):
        return np.arctan2(self._d[1] - self._s[1], self._d[0] - self._s[0])

    def _dronevArr(self):
        return self._driveVelocity * np.array(
            [np.cos(self.sdAngle), np.sin(self.sdAngle)]
        )

    def droneMove(self, t: float):
        sectionTime = t - self._startTime
        self._drone = self._s + self._dronevArr() * sectionTime

    def changeDestination(self):
        self._s = self._d
        self._drone = self._s
        self._d = np.random.rand(2) * [self._A, self._B]
