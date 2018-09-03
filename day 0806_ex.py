#다음과 같이 총 5줄로 구성된 input.txt 파일이 있다.
#모든 숫자를 읽어 총합과 평균을 구하고 화면에 출력하시오.
#result.txt 파일에는 평균을 출력하시오.

#input.txt파일의 내용
# 70
# 55
# 90
# 87
# 38

f=open("input.txt", "r")
lines=f.readlines()
f.close()

print(lines)
#
# for line in lines:
#     sum=sum+int(line)
# print(sum)
sum = 0
avr = 0

for line in lines:
    sum=sum+int(line)
print(sum)

avg=sum/len(lines)

f=open("result.txt", "w")
f.write(str(sum))
f.close()

f=open("input.txt","r")
print(avg)

# def sum(*v) :
#     for i in v :
#         sum+=i
#     return sum
#     f.write(str(sum))
#     f.close()
# print("모든 값의 합계는 %d 입니다." %sum)

#
# def avr(*v) :
#
#     for i in v:
#         avr=avr+i/len(lines)
#     return avr
#     f.write(avr)
#     f.close()
# print("모든 값의 평균은 %d 입니다." %avr)
#
#
