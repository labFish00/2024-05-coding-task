from sim import Sim

A = 10000  # サービスエリアの横幅(m)
B = 10000  # サービスエリアの縦幅(m)

V = 10  # ドローンの移動距離(s)

print("result:", Sim(A, B, V, 300).main())
