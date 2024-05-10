import random
from lib.dronePos import DronePos
from lib.destinationPos import DestinationPos


class Drone:
    def _rand(self, a: int):
        return random.uniform(0, a)

    def __init__(self, a: int, b: int):
        self._A = a
        self._B = b
        self._s = DestinationPos(self._rand(a), self._rand(b))
        self._d = DestinationPos(self._rand(a), self._rand(b))
        self._drone = DronePos(self.getDPos()[0], self.getDPos()[1])

    def getDronePos(self):
        return self._drone.getDronePos()

    def getSPos(self):
        return self._s.getDestinationPos()

    def getDPos(self):
        return self._d.getDestinationPos()

    def changeDestination(self):
        self._s = self._d
        self._d = DestinationPos(self._rand(self._A), self._rand(self._B))
        self._drone = DronePos(self.getSPos()[0], self.getSPos()[1])
