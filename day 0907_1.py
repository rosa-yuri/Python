# 집계함수(aggregate function: sum)
# axis(축)을 지정. 기본값 : None(전체)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
# 1) axis=None, 행렬 전체를 하나의 배열로 보고 집계 연산(sum) 수행 ...45
# 2) axis=0, 각 행의 동일한 인덱스(0,1,2)의 요소를 하나의 배열로 보고 집계연산을 수행 ...12 15 18
# 3) axis=1, 각 행의 열 값들에 대한 집계연산 수행 ...6 15 24

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#
# a=np.arange(1,10).reshape(3,3)
# print(a)
# print()
# print("sum 집계함수")
# print(np.sum(np.sum(a)))
# print(np.sum(a,axis=0))
# print(np.sum(a,axis=1))
# print()
#
# #max(): 가장 큰 수
# print("max() 가장 큰 수 구하기")
# print(np.max(a))
# print(np.max(a, axis=0)) #각 행의 동일한 인덱스의 요소를 비교하여 가장 큰 수를 연산
# print(np.max(a, axis=1)) #각 열의 요소를 비교하여 가장 큰 수를 연산
# print()
#
# #cumsum(): 누적합계
# #np.cumsum(a, axis=0) <-> a.cumsum(axis=0)
# print("cumsum 누적합계")
# print(np.cumsum(a))
# print(np.cumsum(a, axis=0))
# print(np.cumsum(a, axis=1))
# print()
# #
# print("median: 중앙값")
# print("a의 중앙 값", np.median(a))
# print("a의 동일한 인덱스 중앙값", np.median(a, axis=0))
# print("a의 열의 중앙값", np.median(a, axis=1))
#
# b=np.arange(1,5).reshape(2,2)
# print("b의 평균",np.median(b))
# print()
#
# #std():
# print("std: 표준편차")
# print("", np.std(a))
# print("", np.std(a, axis=0))
# print("", np.std(a, axis=1))

#broadcasting
print("broadcasting")
a=np.arange(1,25).reshape(4,6)
b=np.arange(25,49).reshape(4,6)
print(a+b)
print("array[a]와 scala[100]의 합계\n",a+100)
#
# new_arr=np.full_like(a,10)
# print(a+new_arr)
# print(a+10)
# print()
#
# a=np.arange(5)
# print(a)
# a=np.arange(5).reshape((1,5))
# b=np.arange(5).reshape((5,1))
# print(a)
# print(b)
# print(a+b)
#
# print("")
# a=np.random.randint(0,9,(3,3))
# print(a)
# a1=np.copy(a)
# a1[:,0]=99
# print(a1)
# print(a)
#
# import random
# random.seed()
#
# uns=np.random.random((3,3))
# print(uns)
# uns1=uns
# uns2=uns
# uns3=uns
# print("="*50)
# uns1.sort(axis=0)
# #axis 값을 따로 주지 않는 경우,
# # 마지막 축이 기준임(행렬의 경우, (행,열), 3차원(행,열,깊이)의 마지막 축인 열과 깊이의 기준으로 정렬이 됨)
# print(uns1)
#
# a=np.array([40,30,10,20])
# j=np.argsort(a)
# print("a를 오름차순으로 정렬하여 인덱스 번호로 출력:\n",j)
# print("a를 오름차순으로 정렬: ",a[j])
# x=np.array([14,13,11,15,12,16,10])
# print(np.argsort(-x)) #x를 내림차순으로 정렬하여 인덱스 번호로 출력
# print(x[np.argsort(-x)]) #x를 내림차순으로 정렬
# print(np.sort(x))   #정렬 결과만 사본으로 리턴
# print(np.sort(x)[::-1]) #x를 내림차순으로 정렬
# print(x)
# x.sort()
# print(x)

#
# arr=np.arange(0,2*3*4) #0~23(24개)
# v=arr.reshape([2,3,4]) #1차원을 3차원으로 변환: 행(row),열(col),깊이(dep)
# print(v)
# print("총합:",v.sum())
# print("rank:",v.ndim)
#
# res=v.sum(axis=0)
# print("v의 합(정렬 0) shape:",res.shape)
# print("v의 합(정렬 0): \n",res)
#
# res1=v.sum(axis=1)
# print("v의 합(정렬 1) shape:",res1.shape)
# print("v의 합(정렬 1): \n",res)
#
# res2=v.sum(axis=2)
# print("v의 합(정렬 2) shape:",res2.shape)
# print("v의 합(정렬 2): \n",res)
#

