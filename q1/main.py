from drone import Drone

A = 10000  # サービスエリアの横幅(m)
B = 10000  # サービスエリアの縦幅(m)

V = 10  # ドローンの移動距離(s)

n1 = Drone(A, B, V)

print(n1.s)
print(n1.d)
print(n1.driveDistance)
print(n1.driveTime)
print(n1.sdAngle)
n1.droneMove(200)
print(n1.drone)
