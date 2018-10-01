
#퀴즈4. 322쪽 10번문제
#심화퀴즈. GIF 영상의 R,G,B값 각각의 최대출현, 최소출현 R,G,B각각의 평균값, 중위수

from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
import operator


#함수선언
def openFile():
    global photo
    filename = askopenfilename(parent=window, filetypes=(("GIF","*.gif"),("모든파일","*.*")))
    photo = PhotoImage(file=filename)
    plabel.configure(image=photo)
    plabel.image = photo

def exitFile():
    window.quit()
    window.destroy()

def editFile(num):
    global photo
    if num == 1 :
        value = askinteger('확대배수', '숫자(1~4)를 입력하세요', minvalue=1, maxvalue=4)
        plabel.configure(text=str(value))
        photo = photo.zoom(value, value)
        plabel.configure(image=photo)
        plabel.image = photo
    else:
        value = askinteger('축소배수', '숫자(1~4)를 입력하세요', minvalue=1, maxvalue=4)
        plabel.configure(text=str(value))
        photo = photo.subsample(value,value)
        plabel.configure(image=photo)
        plabel.image = photo
    return photo


def analyzeGIF():
    global photo
    rDic, bDic, gDic = {}, {}, {}  #색상:갯수
    xSize = photo.width()
    ySize = photo.height()
    for i in range(xSize):
        for k in range(ySize):
            r,g,b =photo.get(i,k)
            if r in rDic:
                rDic[r] += 1
            else:
                rDic[r] = 1
            if g in gDic:
                gDic[g] +=1
            else:
                gDic[g] = 1
            if b in bDic:
                bDic[b] +=1
            else:
                bDic[b] = 1
    rcountList = sorted(rDic.items(), key=operator.itemgetter(1))
    gcountList = sorted(gDic.items(), key=operator.itemgetter(1))
    bcountList = sorted(bDic.items(), key=operator.itemgetter(1))
    print('최소/최다출현 r픽셀값: ', rcountList[0], rcountList[-1])
    print('최소/최다출현 g픽셀값: ', gcountList[0], gcountList[-1])
    print('최소/최다출현 b픽셀값: ', bcountList[0], bcountList[-1])

    rSum = 0
    for item in rcountList:
        rSum +=item[0]*item[1]
    rAvg = rSum / (xSize*ySize)
    gSum = 0
    for item in gcountList:
        gSum +=item[0]*item[1]
    gAvg = gSum / (xSize*ySize)
    bSum = 0
    for item in bcountList:
        bSum +=item[0]*item[1]
    bAvg = bSum / (xSize*ySize)

    print('r,g,b 필셀 평균값: ', rAvg, gAvg, bAvg)

    rcountList = sorted(rDic.items(), key=operator.itemgetter(0))
    gcountList = sorted(gDic.items(), key=operator.itemgetter(0))
    bcountList = sorted(bDic.items(), key=operator.itemgetter(0))
    rStream, gStream, bStream= [], [], []
    for item in rcountList:
        for i in range(item[1]):
            rStream.append(item[0])
    for item in gcountList:
        for i in range(item[1]):
            gStream.append(item[0])
    for item in bcountList:
        for i in range(item[1]):
            bStream.append(item[0])
    midPos = int((xSize*ySize)/2)
    print('r,g,b픽셀 중위수: ', rStream[midPos], gStream[midPos], bStream[midPos] )



#메인코드
window = Tk()
window.geometry('400x400')

##빈 사진 준비
photo = PhotoImage()
plabel=Label(window, image=photo)
plabel.pack(expand=1, anchor=CENTER)


##메뉴
mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label='열기(Ctrl+0)', command=openFile)
fileMenu.add_separator()
fileMenu.add_command(label='종료(Ctrl+x)', command=exitFile)

editMenu = Menu(mainMenu)
mainMenu.add_cascade(label='이미지효과', menu=editMenu)
editMenu.add_command(label='확대하기', command=lambda :editFile(1))
editMenu.add_command(label='축소하기', command=lambda : editFile(2))

analyzeMenu = Menu(mainMenu)
mainMenu.add_cascade(label='데이터분석', menu=analyzeMenu)
analyzeMenu.add_separator()
analyzeMenu.add_command(label='GIF 데이터분석', command=analyzeGIF)


window.mainloop()



