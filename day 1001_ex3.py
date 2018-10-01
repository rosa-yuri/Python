#퀴즈3. 323쪽 동물 투표

from tkinter import *
from tkinter.filedialog import *

window = Tk()
window.geometry('400x400')
window.title('좋아하는 음식은?')

def image():
    if var.get() == 1:
        photo = PhotoImage(file='D:\Data_study\python_study/bibimicon/bibim.gif')
    elif var.get() == 2:
        photo = PhotoImage(file='D:\Data_study\python_study/bibimicon/chicken2.gif')
    elif var.get() == 3:
        photo = PhotoImage(file='D:\Data_study\python_study/bibimicon/chicken.gif')
    else:
        photo = PhotoImage(file='D:\Data_study\python_study/bibimicon/budae.gif')
    plabel.configure(image=photo)
    plabel.image = photo

##빈 사진 준비
photo = PhotoImage()
plabel = Label(window, image=photo, width=250, height=250)
plabel.pack(expand=1, anchor=CENTER)

#버튼
var=IntVar()
cb1 = Radiobutton(window, text ="비빔밥", fg ="black", bg="#5CD1E5", width=10, variable= var, value=1)
cb2 = Radiobutton(window, text ="닭도리탕", fg ="black", bg="#5CD1E5", width=10, variable =var, value=2)
cb3 = Radiobutton(window, text ="닭갈비", fg ="black", bg="#5CD1E5", width=10, variable =var,  value=3)
cb4 = Radiobutton(window, text ="부대찌게", fg ="black", bg="#5CD1E5", width=10, variable =var, value=4)
res = Button(window, text ="사진보기",fg ="#5CD1E5", bg="black", width=10, command=image)

#패킹
cb1.pack()
cb2.pack()
cb3.pack()
cb4.pack()
res.pack()

window.mainloop()

