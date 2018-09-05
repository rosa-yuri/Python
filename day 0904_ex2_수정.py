#몸풀기문제) 2**1000에 들어가는 숫자들의 합을 구하시오.
a=list(str(2**1000))
print([i for i in str(2**1000)])
print([i for i in a])
print([int(i) for i in a])
print(sum([int(i) for i in a])) #결과값 1366


#1) 1~100000 사이에 있는 7의 개수를 세어보세요.
print(str([i for i in range(1,100001)]).count('7')) #결과값: 50000



a=str([i for i in range(1,100001)])
# print(a)
print(a.count('7')) #결과값: 50000


#2) maria 딕셔너리에 저장된 점수의 평균을 출력하세요
maria={'kor':94, 'eng':91, 'match':89, 'sci':83}
# a=list(maria[i] for i in maria)
# print(sum(a)/len(a))   #결과값: 89.25 (총합 357)
print(sum([int(maria[i]) for i in maria])/len(maria))

#3) 어떤 자연수 n이 있을 때, d(n)을 n의 각 자릿수 숫자들과 n 자신을 더한 숫자라고 정의하자.
#예를 들어 d(91) = 9 + 1 + 91 = 101이고, 이 때, n을 d(n)의 제네레이터라고 한다. 즉 91은 101의 제네레이터이다.
#어떤 숫자들은 하나 이상의 제네레이터를 가지고 있는데, 101의 제네레이터는 91 뿐 아니라 100도 있다.
#그런데 반대로, 제네레이터가 없는 숫자들도 있으며, 이런 숫자를 셀프 넘버(self-number)라 한다.
# 예를 들어 1,3,5,7,9,20,31 은 셀프 넘버들이다.1 이상이고 5000 보다 작은 모든 셀프 넘버들의 합을 구하라.

k=0
x=[]
for n in range(1,5000):
   for i in str(n):
    k += int(i)
    r= k+n
    if r != n:
      x.append(n)
print(sum(set(x)))

#결과값 12497500



# i=456
# for t in str(i):
#     print(int(t)+1)
# print(set(range(1,5))-set(range(1,3)))
# print(sum(set(range(1,5))-set(range(1,3))))


