import numpy as np
# a1=np.arange(24)
# a2=np.arange(24).reshape((4,6))
# a3=np.arange(24).reshape((2,4,3))
# a1[5]=1000
# a2[0,1]=1000
# a3[1,0,1]=1000
# print(a2)
#
# #a2에서 7~10,13~16을 추출하여 출력
# print(a2[1:3,1:5])
# print(a2[1:-1,1:-1])
# # 결과는 동일함 [[ 7  8  9 10] [13 14 15 16]]
#
# print(a2[1:3,1:5])
# print(a2[:,1:3])
# a2[:,1:3]=99
# print(a2)
#
# #짝수뽑기
# a1=np.arange(1,25).reshape(4,6)
# even_a=a1%2==0
# print(a1[even_a])

a=np.arange(1,25).reshape((4,6))
# 팬시 인덱싱: 배열에 인덱스 배열을 전달하여 데이터를 참조하는 것
print(a[0,0],a[1,1],a[2,2],a[3,3])
print(a[[0,1,2,3],[0,1,2,3]])
print(a)
print(a[:,[1,2]])


# #ravel(배열을 1차원으로), reshape메서드- 배열 형태 변경
# a=np.random.randint(1,10,(2,6))
# print(a)
# print("ravel로 보기:",a.ravel())
# print(a)

# #배열 변경, 삭제, 추가 ...
#resize: 배열크기변경(요소 수 변경o)
#reshape:배열모양변경(요소 수 변경x)

# print("a의 모양:",a.shape)
# a.resize((6,2))
# print(a)
# a.resize(2,2)
# print(a)
# a.resize(2,10)
# print(a)
# a.resize((3,3))
# print(a)
#
# # ((a,b)) == (a,b)
# # 현재 버전에서는 함수가 자동으로 적용되서 소괄호 1개로도 충분하지만,
# # 기존 버전에서는 오류가 남. 원칙적으로 ((튜플,튜플))형태임. (요소,요소)임
#
# a=np.arange(1,10).reshape(3,3)
# b=np.arange(10,19).reshape(3,3)
#
# res=np.append(a,b)  #axis 값의 없을 경우 default값으로 1차원 배열이 생성됨
# print(res)
# print(a)    #np.append()는 사본의 형태로 만들어짐. 원본은 수정x
#
# res1=np.append(a,b, axis=0)
# print(res1)
#
# res2=np.append(a,b, axis=1) #열방향, 2차원 배열
# print(res2)
#
# print("="*50)
# # res3=np.arange(10,20).reshape(2,5)
# # print(res3)
# # np.append(a,res3, axis=0)  #오류남
# #append는 기준축과 상대축의 shape 모양이 같은 것만 가능
#
# a=np.arange(1,10).reshape(3,3)
# a=np.insert(a,2,99, axis=0) #2차원 배열에서 2행의 모든 요소 99로 변경
# a=np.insert(a,1,99, axis=1) #2차원 배열에서 각 행의 1번째요소 99로 변경
# a=np.insert(a,1,99) #[ 1 99  2  3  4  5  6  7  8  9]
# print(a)
# print(np.delete(a,1))
#
# #a배열의 1번 인덱스 행 제거 후 출력
# print(np.delete(a,1,axis=0))
#
# #a배열의 1번 인덱스 열 제거 후 출력
# print(np.delete(a,1,axis=1))
#
# print("="*50)
# #concatenate() : 배열 결합
# #vstack(), hstack(): 배열 결합
#
# a=np.arange(1,7).reshape((2,3))
# b=np.arange(7,13).reshape((2,3))
# res1=np.append(a,b,axis=0)
# print(res1)
# print()
# res2=np.concatenate((a,b))
# print(res2)
# print()
# print(np.vstack((a,b)))
# print()
# print(np.hstack((a,b)))
#
# print("="*50)
# a=np.arange(1,25).reshape(4,6)
# # res=np.hsplit(a,3)
# res=np.vsplit(a,2)
# print(res)
#
# x=np.array([1,2])   #list를 array함수에 넣음
# print(x.dtype)
# x=np.array([1.,2.])
# print(x.dtype)
# x=np.array([1,2],dtype=np.int64)
# print(x.dtype)
#
#
# x=np.array([[1,2],[3,4]])
# y=np.array([[5,6],[7,8]])
# v=np.array([9,10])
# w=np.array([11,12])
#
# #행렬 곱
# print(np.dot(x,y)) #[[19 22] [43 50]] ...
#
# #행렬과 벡터의 곱
# print(x.dot(v)) #[29 67] ..1*9+2*10, 3*9+4*10
#
# #벡터의 내적구하기>>
# print(np.dot(v,w))  #9*10_10*12 =219
# print()
#
# x=np.array([[1,2],[3,4]])
# print(x.T)  #T 속성: 대각의 요소를 대칭
# print()
# x=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
# print(x)
# v=np.array([1,0,1])
# vv=np.tile(v,(4,1))
# print(vv)
# # y=np.empty_like(x)
# # print(y)
# # for i in range(4):
# #     y[i,:]=x[i,:]+v #[2,2,4]=[1,2,3]+[1,0,1]
# # print(y)
#
# a=np.array([[1,2],[4,5]])
# # s=np.prod(a)    #모든 요소의 곱셈 .. 40
# # s=np.prod(a, axis=0)    #행의 곱셈.. [4 10]
# # s=np.prod(a, axis=1)    #열의 곱셈.. [2 20]
# # s=np.max(np.prod(a,axis=0)) #행 곱셈 후 요소 중 가장 큰 값
# s=np.max(np.prod(a,axis=1)) #열 곱셈 후 요소 중 가장 큰 값
# print(s)
