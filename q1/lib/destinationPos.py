class DestinationPos:
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    def getDestinationPos(self):
        return (self._x, self._y)

    def setDestinationPos(self, x: float, y: float):
        self._x = x
        self._y = y
