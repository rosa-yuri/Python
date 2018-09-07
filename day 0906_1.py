import numpy as np
print(np.__version__)

list1=[1,2,3,4]
print("list=",list1)
a=np.array(list1)
print("array=",a)
print(a.shape)  #(4,)
print(a[2])

b=np.array([[1,2,3,],[4,5,6]])
print(b)
print(b.shape)  #(2, 3)
print(b[0,0])
print(type(b))  #<class 'numpy.ndarray'>
print(type(list1))  #<class 'list'>

# 벡터화 연산
# 개념 : 배열의 각 요소에 대한 반복 연산을 하나의 명령으로 처리
# 벡터화 연산을 하지 않은 일반적인 반복문 연산(속도 느림)
data = [1, 2, 3, 4, 5]
ans = []
for i in data :
    ans.append(2*i)
print(ans)  #[2, 4, 6, 8, 10]

#벡터화 연산(for 반목문이 없음) -> 속도 무척 빠름
x=np.array(data)
print(2*x) #x는 array    ...[ 2  4  6  8 10]
print(2*data) #data는 list   ...[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

a=np.array([1,2,3])
b=np.array([10,20,30])
print(a*2+b)    #[12 24 36]
print(a==2) #[False  True False]
print(b>10) #[False  True  True]
print((a==2)&(b>10))    #[False  True False]
print(a.shape)  #shape
print(a.ndim)   #rank
print(a.dtype)  #int32 ... 정수 32bit임

a=np.zeros(4)
print(a)    #[0. 0. 0. 0.]
print(type(a))  #자료구조... <class 'numpy.ndarray'>
print(a.dtype)  #자료형태... float64    실수 64bit

a=np.zeros((2,2))
print(a)    #[[0. 0.] [0. 0.]]
a=np.ones((2,3))
print(a)    #[[1. 1. 1.] [1. 1. 1.]]
a=np.full((2,3),5)
print(a)    #[[5 5 5] [5 5 5]]
a=np.eye(5)
print(a)    #[[1. 0. 0. 0. 0.] [0. 1. 0. 0. 0.] [0. 0. 1. 0. 0.] [0. 0. 0. 1. 0.] [0. 0. 0. 0. 1.]]

print(np.array(range(20)))
print(np.array(range(20)).reshape(4,5))

c=np.array(range(20)).reshape(4,5)
print(len(c))   #행의 개수, 4
print(len(c[0])) #0번째 열의 길이 = 0번 열에 있는 값(요소)의 개수, 5

print(c.ndim)    #rank:2
print(c.shape) #shape:(4,5)

print(c)
print("="*50)
print(c>10)
print("="*50)
print(c[c>10])

c[c>10]=99
print(c)

arr=np.arange(0, 3*2*4)
print(arr)
print(len(arr))
v=arr.reshape([3,2,4])  #[depth, row, collum]
print(v)
print(len(v))
print(len(v[0]))
print(len(v[0][0]))

a=np.arange(0, 3*4)
a=a.reshape([3,4])
print(a)

b=np.array([0,1,2,3,4])
print(b[2])
print(b[-1])
#다차원 배열을 슬라이싱할 때 사용되는 콤마(,)로 차원을 구분(축)

print(a)
print(a[0,1])
print(a[-1,-1])

#인덱싱: 행 지정, 슬라이싱: 추출 열 지정
print(a[0, :])  #첫번재 행 전체를 추출
print(a[:,1])  #두번째 열 전체를 추출
print(a[1,1:])  #두번째 행의 두번째 열부터 끝열까지 추출
print(a[:2,:2])
print(a[1, :])
print(a[1:2, :])

a=np.array([[1,2],[3,4],[5,6]])
print(a.shape)
print(a)
print(a[0,0])
print(a[[0,1,2],[0,1,0]])   #array 형태로 나옴 ...[1 4 5]
print(a[0,0], a[1,1], a[2,0])   #scala 형태로 나옴 ...1 4 5
print(type([a[0,0], a[1,1], a[2,0]]))    #<class 'list'>
print(np.array([a[0,0], a[1,1], a[2,0]]))  #[1 4 5]
print(type(np.array([a[0,0], a[1,1], a[2,0]]))) #<class 'numpy.ndarray'>

a=np.array([[1,2],[3,4],[5,6]])
print(a[0,0], a[1,1], a[2,0])

#list -> np.array -> array -> reshape -> indexing
#임의의 numpy 배열 'a[[row1,row2],[col1,col2]]'는 a[row1,col1]과 a[row2, col2]라는 두 개의 배열의 요소의 집합

a=np.array([[1,2],[3,4],[5,6]])
s=a[[0,2],[1,1]]
print(s)
lst=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
x=np.array(lst)

bool_ind=x%2
print(bool_ind)
bool_ind=x%2 == 0
print(bool_ind)
print(x[bool_ind])
print(x[x%2==0])

# bool_ind_arr=np.array([
#     [False, True, False],
#     [True, False, True],
#     [False, True, False],
# ])
# print(type(lst))
# print(type(bool_ind_arr))
#
# res=x[bool_ind_arr]
# print(res)