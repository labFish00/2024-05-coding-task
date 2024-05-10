from drone import Drone

A = 10000  # サービスエリアの横幅(m)
B = 10000  # サービスエリアの縦幅(m)

V = 10  # ドローンの移動距離(s)

n1 = Drone(A, B)

print(n1.getDronePos())
print(n1.getSPos())
print(n1.getDPos())
