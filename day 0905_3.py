import numpy as np

trees=np.loadtxt('Data/trees.csv', delimiter=',', skiprows=1, unpack=True)
#skiprows= 실행하지 않고 지나갈 행의 개수
#unpack=True (3행 31열), False(31행 3열)
print(trees.shape)

print("="*50)
print(trees[:-1])

print("="*50)
print(trees[[-1]])