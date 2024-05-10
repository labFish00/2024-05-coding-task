class DronePos:
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    def getDronePos(self):
        return (self._x, self._y)

    def updateDronePos(self, x: float, y: float):
        self._x = self._x + x
        self._y = self._y + y

    def setDronePos(self, x: float, y: float):
        self._x = x
        self._y = y
