import numpy as np
import numpy.typing as npt


class Drone:
    _startTime = 0.0
    _change = 1

    def __init__(self, a: int, b: int, v: int):
        self._A = a
        self._B = b
        self._s = np.random.rand(2) * [a, b]
        self._d = np.random.rand(2) * [a, b]
        self.drone = self._s
        self._driveVelocity = v

    @property
    def change(self):
        return self._change

    def _droneMove(self, t: float):
        sdAngle = np.arctan2(self._d[1] - self._s[1], self._d[0] - self._s[0])
        dronevArr = self._driveVelocity * np.array([np.cos(sdAngle), np.sin(sdAngle)])
        sectionTime = t - self._startTime
        self.drone = self._s + dronevArr * sectionTime

    def _changeDestination(self):
        self._startTime += np.linalg.norm(self._s - self._d) / self._driveVelocity
        self._s = self._d
        self.drone = self._d
        self._d = np.random.rand(2) * [self._A, self._B]
        self._change += 1

    def advanceTime(self, t: float):
        if t < self._startTime:
            raise ValueError("Time cannot go backwards")

        while t - self._startTime > (
            np.linalg.norm(self._s - self._d) / self._driveVelocity
        ):
            self._changeDestination()

        self._droneMove(t)
