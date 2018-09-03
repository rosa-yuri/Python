from tkinter import *
from tkinter import messagebox
window = Tk()

def myFunc1() :
    if chk1.get() == 0 :
        messagebox.showinfo("메뉴 선택 확인","해물떡볶이를 취소했습니다")
    elif chk1.get() == 1 :
        messagebox.showinfo("메뉴 선택 확인","해물떡볶이를 선택했습니다")
def myFunc2():
    if chk2.get() == 0 :
        messagebox.showinfo("메뉴 선택 확인","알밥을 취소했습니다")
    elif chk2.get() == 1:
        messagebox.showinfo("메뉴 선택 확인","알밥을 선택했습니다")

def myFunc3():
    if chk3.get() == 0 :
        messagebox.showinfo("메뉴 선택 확인","육회비빔밥을 취소했습니다")
    elif chk3.get() == 1:
        messagebox.showinfo("메뉴 선택 확인","육회비빔밥를 선택했습니다")

def myFunc4():
    if chk4.get() == 0 :
        messagebox.showinfo("메뉴 선택 확인","도루묵구이를 취소했습니다")
    elif chk4.get() == 1:
        messagebox.showinfo("메뉴 선택 확인","도루묵구이를 선택했습니다")

chk1=IntVar()
chk2=IntVar() #정수형 변수
chk3=IntVar()
chk4=IntVar()
cb1 = Checkbutton(window, text ="해물떡볶이", fg ="black", bg="#5CD1E5", width=10, variable =chk1,  command=myFunc1)
cb2 = Checkbutton(window, text ="알밥", fg ="black", bg="#5CD1E5", width=10, variable =chk2, command=myFunc2)
cb3 = Checkbutton(window, text ="육회비빔밥", fg ="black", bg="#5CD1E5", width=10, variable =chk3,  command=myFunc3)
cb4 = Checkbutton(window, text ="도루묵구이", fg ="black", bg="#5CD1E5", width=10, variable =chk4, command=myFunc4)

cb1.pack()
cb2.pack()
cb3.pack()
cb4.pack()


window.mainloop()