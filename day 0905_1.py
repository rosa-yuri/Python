path="example.txt"
data=open(path).readline()
# print(data)

import json
path="example.txt"
records=[json.loads(line) for line in open(path, encoding='utf-8')]
# print(records[0])
# print(records[0]['tz'])

time_zones=[ rec['tz'] for rec in records if 'tz' in rec]
# print(time_zones)

print(time_zones[:20])

def get_counts(sequence):
    counts={}
    for x in sequence:
        if x in counts: #도시명이 이미 저장되어 있는 경우
            counts[x]+=1
        else:           #저장 안되어 있는 경우
            counts[x]=1
    return counts

from collections import defaultdict

def get_counts2(sequence):
    counts=defaultdict(int) #defaultdict(int)는 0으로 초기화
    for x in sequence:
        counts[x]+=1
    return counts

# counts=get_counts(time_zones)
counts=get_counts2(time_zones)
# print(counts)
# print(type(counts))
# print(counts['America/New_York'])
# print(len(counts))      #도시의 개수(97)
# print(len(time_zones))  #'tz'가 있는 행의 개수(3440)

#가장 많이 등장한 도시 10개를 출력하기
def top_counts(count_dict, n=10):
    value_key_pairs=[(value,key) for key,value in count_dict.items()]
    print(value_key_pairs)
    value_key_pairs.sort()
    print(value_key_pairs[-n:])

top_counts(counts,10)  #상위 10개 도시 출력

from collections import Counter
counts=Counter(time_zones)
# print(counts.most_common(10))   #Counter 함수 이용해서 상위 10개 도시 출력. 자동으로 내림차순 정렬되어 출력됨
# print(counts)

eng="sdkfahfoie4kgndkalfjdia"
# print(Counter(eng))
#출력값 Counter({'d': 3, 'k': 3, 'f': 3, 'a': 3, 'i': 2, 's': 1, 'h': 1, 'o': 1, 'e': 1, '4': 1, 'g': 1, 'n': 1, 'l': 1, 'j': 1})


#Pandas란? 데이터 분석 패키지: 모듈(.py; 함수, 클래스, 변수 등 구성요소의 묶음) 또는 패키지의 붂음

from pandas import DataFrame, Series
import pandas as pd
# print(records)
frame=DataFrame(records)    #Data를 표(table) 형태로 변환
print(type(frame))
# print(frame)
# print(frame.info())
# print(type(frame['tz'][-10:]))

tz_counts=frame['tz'].value_counts()
# print(tz_counts)


#tz 키가 존재하지 않는 경우
clean_tz=frame['tz'].fillna('Missing') #Null 항목없음
# print(clean_tz)
#na: Not Available(결측값)
#tz 키는 존재하나 값이 없는 경ㅇ우(결측값)
clean_tz[clean_tz=='']='Unkown' #N/A 누락
# print(clean_tz)
tz_counts=clean_tz.value_counts()
print(tz_counts)

import matplotlib.pyplot as plt
tz_counts[:10].plot(kind='barh')
# plt.show()


# print(frame.a.dropna()) #na행이 제거됨

results=Series([x.split()[0] for x in frame.a.dropna()])
# print(type(results))
# print(results.value_counts()[:5])

# print(frame[frame.a.notnull()])
# print(len(results))

#a키 값이 windows를 포함하면 -> Windows, 포함되지 않는 경우 -> Not Windows로 변경
cframe=frame[frame.a.notnull()]
# print(cframe)   #a키가 없는 행은 제거된 상태

print(cframe.a)   # <=> print(cframe['a'])


import numpy as np

print(cframe.a.str.contains('Windows'))
os=np.where(cframe.a.str.contains('Windows'), 'Windows', 'Not Windows')
print(os)
by_tz_os=cframe.groupby(['tz', os])   #cframe을 os별로 'tz'값에 따라 그룹화
agg_counts=by_tz_os.size().unstack().fillna(0)
print(agg_counts[-10:])

print(agg_counts[-10:].sum(1))

indexer=agg_counts.sum(1).argsort()
print(indexer[-10:])

count_subset=agg_counts.take(indexer)[-10:]
print(count_subset)
count_subset.plot(kind='barh', stacked=True)

normed_subset=count_subset.div(count_subset.sum(1), axis=0)
print(normed_subset)
normed_subset.plot(kind='barh', stacked=True)
plt.show()