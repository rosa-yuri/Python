import numpy as np
import matplotlib.pyplot as plt

a=np.array([[1,2,3],[4,5,6]])
b=np.ones_like(a)
# print(b)

#데이터 생성 함수
#
# #0~1 범위 내에서 균등 간격으로 5개의 수를 생성하라
# a=np.linspace(0,1,10)    #개수의 default 값은 50
# # print(a)
# # plt.plot(a, 'o')
# # plt.show()
#
# a=np.arange(0,10,1,np.float)
# print(type(a))
# print(a)
# # plt.plot(a,'o')
# # plt.show()
#
# mean=0  #평균
# std=1   #표준편차
# a=np.random.normal(mean, std, 10000)    #정규분포 생성
# print(a)
# plt.hist(a, bins=1000)   #히스토그램
# plt.show()

#균등분포
# a=np.random.rand(10000)
# plt.hist(a, bins=10)
# plt.show()
#
# a=np.random.randint(5,10, size=(3,4))
# print(a)
#
# a=np.random.randint(-100,100, size=10000)
# print(a)
# plt.hist(a, bins=10)
# plt.show()

# a=np.random.randint(0,10,(2,3))
# print("a=",a)
# print("="*50)
# b=np.random.randint(0,10,(2,3))
# print("b=",b)
#
# np.save('myarr1',a) #myarr1.npy ... save()함수는 배열을 바이너리 형태로 저장
# np.savez('myarr2',a,b)
# print("="*50)
#
# print("myarr1=",np.load('myarr1.npy'))
# print("="*50)
# npzfiles=np.load("myarr2.npz")
# print(npzfiles.files)
# print()
# print("arr_0=",npzfiles['arr_0'])
# print()
# print("arr_1=",npzfiles['arr_1'])
# print("myarr2=",np.load('myarr2.npz'))
#
# print("="*50)
# print(np.loadtxt('simple.csv', dtype=np.int))
# # print(np.loadtxt('simple.csv', dtype=np.int, delimiter=" "))
# data=(np.loadtxt('height.csv', delimiter=',', skiprows=1, dtype={
#     'names':('order','name','height(cm)'),
#     'formats':('f','S20','i')   #i:int, f:float
# }))
# print(data) #[(1., b'MJI', 180) (2., b'LMB', 175) (3., b'LSJ', 182) (4., b'CYR', 168)] ... b: binary의 약자
#
# print("="*50)
# #savetxt함수: 배열을 텍스트 팡리로 저장
#
# data=np.random.random((3,4))
# print(data)
# np.savetxt('saved.csv', data, delimiter=',')
# print()
# print(np.loadtxt('saved.csv', delimiter=','))

# arr=np.random.random((5,2,3))   #난수 뽑기. 난수는 default 값으로 0~1 사이에서 나옴.
# print(type(arr))    #자료구조
# print(arr.shape)    #자료모양
# print(len(arr))     #자료길이
# print(arr.ndim)     #rank(차원의 크기)
# print(arr.size)     #자료크기(요소의 개수)
# print(arr)
# print(arr.dtype)    #자료형태
# print(arr.astype(np.int))   #astype은 사본의 자료 dtype만 바꿈
# arr=arr.astype(np.float)
# print(arr)
# print("="*50)
# print(np.info(np.ndarray.dtype))
#
# print("="*50)
# a=np.arange(1,10).reshape(3,3)
# print(a)
# b=np.arange(9,0,-1).reshape(3,3)    #감소할 때는 반드시 뒤에 감소값을 명시해줘야 함. 안그럼 에러남
# print(b)
#
# print("="*50)
# print(a-b)
# print(np.subtract(a,b))
# print()
# print(a+b)
# print(np.add(a,b))
# print()
# print(a/b)
# print(np.divide(a,b))
# print()
# print(a*b)
# print(np.multiply(a,b))
# print()
# print(b)
# print(np.exp(b))
# print()
# print(np.sqrt(a))
# print()
# print(np.sin(a))
# print()
# print(np.cos(a))
# print()
# print(np.tan(a))
# print()
# print(np.log(a))
print("★"*5,"추천시스템 만들때 많이 사용하는것! 꼭 알아두기","★"*5)
a=np.arange(1,10)
b=np.arange(9,0,-1)    #감소할 때는 반드시 뒤에 감소값을 명시해줘야 함. 안그럼 에러남
print()
a=np.arange(1,5).reshape(2,2)
b=np.arange(9,5,-1).reshape(2,2)
print()
print(a)
print(b)
print()
print(np.dot(a,b))  #벡터 내적구하기
print(type(a==b))

print(np.array_equal(a,b))

print(np.sum(a))
print("="*50)
print(a)
print(a.sum(axis=0))
#axis=0, 행을 기준으로 각 행의 동일한 인덱스 요소를 그룹화해라
print(a.sum(axis=1))
#axis=1, 열을 기준으로 각 행의 동일한 인덱스 요소를 그룹화해라

