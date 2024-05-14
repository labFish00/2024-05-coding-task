import numpy as np
from drone import Drone

A = 10000
B = 10000
V = 10
rang = 300

contacted = False
topCount = 0
buttomCount = 0


def check_distace(distance):
    return rang > distance


def counter(contact: bool):
    global contacted
    global topCount
    global buttomCount
    if contact:
        contacted = True
    else:
        if contacted:
            buttomCount += 1
        topCount += 1
        contacted = False


def main():
    n1 = Drone(A, B, V)
    n2 = Drone(A, B, V)

    n1route = []
    n2route = []
    distances = []
    contacts = []

    for i in range(1, 1000000):
        t = i
        n1.advanceTime(t)
        n2.advanceTime(t)
        n1route.append(n1.drone)
        n2route.append(n2.drone)

    distances = np.linalg.norm(np.array(n1route) - np.array(n2route), axis=1)
    contacts = distances < rang

    for contact in contacts:
        counter(contact)

    print(topCount / buttomCount)
    print(topCount)
    print(buttomCount)


if __name__ == "__main__":
    main()
