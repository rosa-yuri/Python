#아래와 같은 결과가 출력되는 정규식을 만드세요

"""
True True True True True False False False

emails = ['python@mail.example.com', 'python+kr@example.com',              # 올바른 형식
          'python-dojang@example.co.kr', 'python_10@example.info',         # 올바른 형식
          'python.dojang@e-xample.com',                                    # 올바른 형식
          '@example.com', 'python@example', 'python@example-com']          # 잘못된 형식
"""

import re

res=[]
emails=['python@mail.example.com', 'python+kr@example.com',
        'python-dojang@example.co.kr','python_10@example.info', 'python.dojang@e-xample.com',
        '@example.com', 'python@example', 'python@example-com']

# pat=re.compile(".+?\w+[@]\w+.+?[.]\w+[.]?\w+")
pat=re.compile(".+?[@].+?[.][.]?\w+")

# pat=re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9]+\.[a-zA-z0-9-.]+$')
"""
아이디@도메인.최상위도메인
"""

for r in emails:
    res = pat.match(r)
    # print(res)
    if res == None :
      print("False")
    else:
      print("True")





