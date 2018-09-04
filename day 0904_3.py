import random
random.seed(999)
for i in range(20):
    print(random.randrange(10))
print(random.randrange(100))

a=[random.randrange(100) for _ in range(10)]
print(a)    #[72, 73, 68, 62, 61, 16, 82, 40, 82, 82]

print([i for i in range(10)])   #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print([i for i in a])   #[72, 73, 68, 62, 61, 16, 82, 40, 82, 82]

print([i for i in a if i%2 == 1])   #[73, 61]
print([i for i in a if i%2])    #[73, 61]
print([i for i in a if i%2][::-1])  #[61, 73]
print([i for i in a[::-1] if i%2])  #[61, 73]
print([i for i in reversed(a) if i%2])  #[61, 73]

#Data -> Train Data(70%) -> Test Data(30%) -> Model -> Test Data 입력 -> 모델 평가 -> Feedback

a1=[random.randrange(100) for _ in range(10)]
a2=[random.randrange(100) for _ in range(10)]
a3=[random.randrange(100) for _ in range(10)]
b=[a1,a2,a3]
print(b)

print(sum([1,3,5]))

print([sum(i) for i in b])
print(sum([sum(i) for i in b]))

print([j for i in b for j in i])    #차원이 감소됨 (축소가 아님)

print([j for i in b for j in i if j % 2])

print([[j for j in i] for i in b])
print([[j for j in i if j % 2] for i in b])

print("="*70)
print(b)
print([i for i in b[::-1]])
print([[j for j in i[::-1]] for i in b[::-1]])


print(2**1000)