from tkinter import*
from time import*

fnameList = ["noodle.gif", "chicken2.gif", "chicken.gif","chicken3.gif", "budae.gif"
             "kimchi.gif", "mak.gif", "pork.gif", "dong.gif"]

photoList = [None]*9
num = 0

def clickNext():
    global num
    num +=1
    if num > 8:
        num=0
    photo = PhotoImage(file="d:/python_study/bibimicon/"+fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image=photo

def clickPrev():
    global num
    num -=1
    if num <0 :
        num =8
    photo =PhotoImage(file ="d:/python_study/bibimicon/"+fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image=photo


window =Tk()
window.geometry("700x500")
window.title("음식보기")

btnPrev=Button(window, text ="<<이전", command =clickPrev)
btnNext=Button(window, text ="다음>>", command =clickNext)

photo=PhotoImage(file ="d:/python_study/bibimicon/"+fnameList[0])
pLabel=Label(window, image=photo)

btnPrev.place(x=250, y=10)
btnNext.place(x=400, y=10)
pLabel.place(x=15,y=50)

window.mainloop()


