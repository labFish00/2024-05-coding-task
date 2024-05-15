import numpy as np
from drone import Drone


class Sim:
    _contacted = False
    _topCount = 0
    _buttomCount = 0

    def __init__(self, a, b, v, rng):
        self._n1 = Drone(a, b, v)
        self._n2 = Drone(a, b, v)
        self._rang = rng

    def check_distace(self, distance):
        return self._rang > distance

    def counter(self, contact: bool):
        if contact:
            self._contacted = True
        else:
            if self._contacted:
                self._buttomCount += 1
            self._topCount += 1
            self._contacted = False

    def main(self):

        T = 1000000
        res = 1

        n1route = []
        n2route = []
        distances = []
        contacts = []

        for i in range(1, T):
            t = i / res
            self._n1.advanceTime(t)
            self._n2.advanceTime(t)
            n1route.append(self._n1.drone)
            n2route.append(self._n2.drone)
            if (i / T) * 100 % 10 == 0:
                print("rang:", self._rang, "progress:", (i / T) * 100, "%")

        distances = np.linalg.norm(np.array(n1route) - np.array(n2route), axis=1)
        contacts = distances < self._rang

        for contact in contacts:
            self.counter(contact)

        print(self._topCount / self._buttomCount)
        print(self._topCount)
        print(self._buttomCount)
        return self._topCount / self._buttomCount
