a=[1,3,5,7,9,0,2,4,6,8]
print(a[::-1])  #[8, 6, 4, 2, 0, 9, 7, 5, 3, 1]
print(a[len(a)-1: :-1]) #[8, 6, 4, 2, 0, 9, 7, 5, 3, 1]
print(a[::-2])  #[8, 4, 0, 7, 3]
print(a[-2 ::-2])   #[6, 2, 9, 5, 1]


import csv

def read_car():
    f=open('Data/cars.csv', 'r')
    rows=[]
    for row in f:
        # print(row)
        rows.append(row.strip().split(','))   #split()은 ()안의 문자열을 기준으로 리스트 요소로 만들어 줌
    f.close()
    return rows

def write_car(rows):
    f=open('Data/car_w.txt','w', newline='')
    wrtier=(csv.writer(f, delimiter=':'))
    for row in rows:
        wrtier.writerow(row)
    f.close()

mycar=read_car()
write_car(mycar)