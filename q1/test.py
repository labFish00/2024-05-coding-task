from drone import Drone
import matplotlib.pyplot as plt

n1 = Drone(10000, 10000, 10)

pos = []

for i in range(50000):
    t = i / 100
    n1.advanceTime(t)
    pos.append(n1.drone)

# 散布図を描画
plt.scatter([p[0] for p in pos], [p[1] for p in pos], s=1)
plt.savefig("sin.png", format="png", dpi=300)
