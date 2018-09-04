import numpy as np      #행렬연산을 빠르게 실행해주는 패키지
a=np.array([1,3,5])     #
print(a)    #[1 3 5]
print(type(a))  #<class 'numpy.ndarray'>

b=np.arange(7)
print(b)    #[0 1 2 3 4 5 6]
b+=1        #[1 1 1 1 1 1 1]
print(b)    #broad casting ..[1 2 3 4 5 6 7]
print(b<4)  #[ True  True  True False False False False]
print(b[b<4])   #[1 2 3]

c=np.arange(3,7,0.1)
print(c)    #[3.  3.1 3.2 3.3 3.4 3.5 3.6 3.7 3.8 3.9 4.  ....  6.1 6.2 6.3 6.4 6.5 6.6 6.7 6.8 6.9]

d=np.arange(15)
print(d)    #[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
print(d.shape)  #((15,)
print(d+1)

d=np.arange(15).reshape(3,5)
print(d)   #[[ 0  1  2  3  4]  [ 5  6  7  8  9]  [10 11 12 13 14]]
print(d.shape) #(3, 5)

print(d[d>5])
print("="*50)
print(d[0])
print(d[-1])
print("="*50)

print(d[0][0])
print(d[0,0])
print("="*50)

print(d[-1][0])
print(d[-1][-1])

print(d[::-1])
print("="*50)

print(d[::-1][::-1])   #[[10 11 12 13 14] [ 5  6  7  8  9] [ 0  1  2  3  4]] [[ 0  1  2  3  4] [ 5  6  7  8  9] [10 11 12 13 14]]
print("="*50)

print(d[::-1, ::-1])   #[[14 13 12 11 10] [ 9  8  7  6  5] [ 4  3  2  1  0]]

print("="*50)
print(d[1:3, 2:4])


print("="*50)

print(d)                #[[ 0  1  2  3  4] [ 5  6  7  8  9] [10 11 12 13 14]]
print(d.sum())          #105
print(d.sum(axis=1))    #[10 35 60] - 각 행의 총합
print(d.sum(axis=0))    #[15 18 21 24 27] 각 열의 총합

# d2=np.arange(24).reshape(2,3,4)
# print(d2)   #[[[ 0  1  2  3] [ 4  5  6  7] [ 8  9 10 11]]  [[12 13 14 15] [16 17 18 19] [20 21 22 23]]]
# print(d2.shape) #(2, 3, 4)
#
# d3=np.arange(48).reshape(2,3,4,2)
# print(d3)
# print(d3.shape) #(2, 3, 4, 2)
