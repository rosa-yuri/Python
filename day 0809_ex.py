# """
# 1. 단어가 줄 단위로 저장된 words.txt 파일이 주어집니다. 다음 소스 코드를 완성하여 10자 이하인 단어의 개수가 출력되게 만드세요.
# 출력 : 4
#
# f=open("words.txt","w")
# data="""anonymously
# compatibility
# dashboard
# experience
# photography
# spotlight
# warehouse"""
# nf=f.write(data)
# f.close()
#
#
with open("words.txt", "r") as file:
    count = 0
    words =file.readlines()
    for word in words:
        if len(word.strip('\n')) <= 10:
            count+=1
    print(count)


# print(re.findall(" "))
# print(nf.find_all("\n"))

# for i in data:
#      if split(" ") < 10 :
#          print([i])



# """
# 2. 표준 입력으로 정수와 문자열이 각 줄에 입력됩니다.
# 다음 소스 코드를 완성하여 입력된 숫자에 해당하는 단어 단위 N-gram을 출력하세요.
# 만약 입력된 문자열의 단어 개수가 입력된 정수 미만이라면 'wrong'을 출력하세요.
#
# 실행 결과
# 7 (입력)
# Python is a programming language that lets you work quickly (입력)
# Python is a programming language that lets
# is a programming language that lets you
# a programming language that lets you work
# programming language that lets you work quickly
# """

# n=int(input("숫자를 입력하세요  "))
# text=input("단어를 입력하세요  ")
# words=text.split()
#
# if(len(words) < n) :
#     print('wrong')
#
# else:
#     for i in range(len(words) - (n-1)):
#         for j in range(n):
#             print(words[i+j], end=' ')
#         print()