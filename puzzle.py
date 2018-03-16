from tkinter import *
from tkinter import messagebox
import random

root = Tk()

frame=Frame(root)

Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
frame.grid(row=0, column=0, sticky=N+S+E+W)
grid=Frame(frame)
grid.grid(sticky=N+S+E+W, column=0, row=7, columnspan=2)
Grid.rowconfigure(frame, 7, weight=1)
Grid.columnconfigure(frame, 0, weight=1)

step=0


def s1():
    global step
    step+=1
    if btn2['text']=="":
        temp=btn1['text']
        btn1['text']=btn2['text']
        btn2['text']=temp
        type(temp)

    elif btn4['text']=="":
        temp=btn1['text']
        btn1['text']=btn4['text']
        btn4['text']=temp
    check_win()
    cost_check()
    


    
def s2():
    global step
    step+=1
    if btn1['text']=="":
        temp=btn2['text']
        btn2['text']=btn1['text']
        btn1['text']=temp

    elif btn3['text']=="":
        temp=btn2['text']
        btn2['text']=btn3['text']
        btn3['text']=temp

    elif btn5['text']=="":
        temp=btn2['text']
        btn2['text']=btn5['text']
        btn5['text']=temp
    cost_check()
    check_win()
    
def s3():
    global step
    step+=1
    if btn2['text']=="":
        temp=btn3['text']
        btn3['text']=btn2['text']
        btn2['text']=temp
        

    elif btn6['text']=="":
        temp=btn3['text']
        btn3['text']=btn6['text']
        btn6['text']=temp
    check_win()
    cost_check()
    
def s4():
    global step
    step+=1
    if btn1['text']=="":
        temp=btn4['text']
        btn4['text']=btn1['text']
        btn1['text']=temp

    elif btn7['text']=="":
        temp=btn7['text']
        btn7['text']=btn4['text']
        btn4['text']=temp

    elif btn5['text']=="":
        temp=btn4['text']
        btn4['text']=btn5['text']
        btn5['text']=temp
    check_win()
    cost_check()
    
def s5():
    global step
    step+=1
    if btn2['text']=="":
        temp=btn2['text']
        btn2['text']=btn5['text']
        btn5['text']=temp

    elif btn4['text']=="":
        temp=btn5['text']
        btn5['text']=btn4['text']
        btn4['text']=temp

    elif btn6['text']=="":
        temp=btn6['text']
        btn6['text']=btn5['text']
        btn5['text']=temp
        
    elif btn8['text']=="":
        temp=btn8['text']
        btn8['text']=btn5['text']
        btn5['text']=temp
    check_win()
    cost_check()
    
def s6():
    global step
    step+=1
    if btn3['text']=="":
        temp=btn3['text']
        btn3['text']=btn6['text']
        btn6['text']=temp

    elif btn5['text']=="":
        temp=btn5['text']
        btn5['text']=btn6['text']
        btn6['text']=temp

    elif btn9['text']=="":
        temp=btn9['text']
        btn9['text']=btn6['text']
        btn6['text']=temp
    check_win()
    cost_check()
    
def s7():
    global step
    step+=1
    if btn4['text']=="":
        temp=btn4['text']
        btn4['text']=btn7['text']
        btn7['text']=temp

    elif btn8['text']=="":
        temp=btn8['text']
        btn8['text']=btn7['text']
        btn7['text']=temp
    check_win()
    cost_check()
    
def s8():
    global step
    step+=1
    if btn7['text']=="":
        temp=btn7['text']
        btn7['text']=btn8['text']
        btn8['text']=temp

    elif btn5['text']=="":
        temp=btn5['text']
        btn5['text']=btn8['text']
        btn8['text']=temp

    elif btn9['text']=="":
        temp=btn9['text']
        btn9['text']=btn8['text']
        btn8['text']=temp
    check_win()
    cost_check()
    
def s9():
    global step
    step+=1
    if btn6['text']=="":
        temp=btn6['text']
        btn6['text']=btn9['text']
        btn9['text']=temp

    elif btn8['text']=="":
        temp=btn8['text']
        btn8['text']=btn9['text']
        btn9['text']=temp
    check_win()
    cost_check()
    

def restart():
    global step
    step=0
    random.choice([p1,p2])()
def p1():
    btn1.configure(text="1")
    btn2.configure(text="2")
    btn3.configure(text="3")
    btn4.configure(text="4")
    btn5.configure(text="")
    btn6.configure(text="5")
    btn7.configure(text="7")
    btn8.configure(text="8")
    btn9.configure(text="6")

def p2():
    btn1.configure(text="2")
    btn2.configure(text="1")
    btn3.configure(text="3")
    btn4.configure(text="4")
    btn5.configure(text="6")
    btn6.configure(text="7")
    btn7.configure(text="8")
    btn8.configure(text="")
    btn9.configure(text="5")

def p3():
    btn1.configure(text="6")
    btn2.configure(text="4")
    btn3.configure(text="7")
    btn4.configure(text="8")
    btn5.configure(text="5")
    btn6.configure(text="")
    btn7.configure(text="3")
    btn8.configure(text="2")
    btn9.configure(text="1")
    

btn1 = Button(frame,command=s1)
btn1.grid(column=0, row=0, sticky=N+S+E+W)
btn2 = Button(frame,command=s2)
btn2.grid(column=1, row=0, sticky=N+S+E+W)
btn3 = Button(frame,command=s3)
btn3.grid(column=2, row=0, sticky=N+S+E+W)
btn4 = Button(frame,command=s4)
btn4.grid(column=0, row=1, sticky=N+S+E+W)
btn5 = Button(frame,command=s5)
btn5.grid(column=1, row=1, sticky=N+S+E+W)
btn6 = Button(frame,command=s6)
btn6.grid(column=2, row=1, sticky=N+S+E+W)
btn7 = Button(frame,command=s7)
btn7.grid(column=0, row=2, sticky=N+S+E+W)
btn8 = Button(frame,command=s8)
btn8.grid(column=1, row=2, sticky=N+S+E+W)
btn9 = Button(frame,command=s9)
btn9.grid(column=2, row=2, sticky=N+S+E+W)
btn10 = Button(frame,text="restart",command=restart)
btn10.grid(column=3, row=0, sticky=N+S+E+W)
random.choice([p1,p3])()


def check_win():
    rule=[btn1['text']=="1" and
          btn2['text']=="2" and
          btn3['text']=="3" and
          btn4['text']=="4" and
          btn5['text']=="5" and
          btn6['text']=="6" and
          btn7['text']=="7" and
          btn8['text']=="8" and
          btn9['text']==""]
    if btn1['text']=="1" and btn2['text']=="2" and btn3['text']=="3" and btn4['text']=="4" and btn5['text']=="5" and btn6['text']=="6" and btn7['text']=="7" and btn8['text']=="8" and btn9['text']=="":

        messagebox.showinfo("you won")
        print('you took',step,'steps')
        
        
def restart():
    random.choice([p1,p2])()

    
def reset():
    btn1['text']=="1"
    btn2['text']=="2"
    btn3['text']=="3"
    btn4['text']=="4"
    btn5['text']=="5"
    btn6['text']=="6"
    btn7['text']=="7"
    btn8['text']=="7"
    btn9['text']==""

def cost_check():
    cost=0
    if btn1['text']=="1":
        cost+=0
    else:
        cost+=1
    if btn2['text']=="2":
        cost+=0
    else:
        cost+=1
    if btn3['text']=="3":
        cost+=0
    else:
        cost+=1
    if btn4['text']=="4":
        cost+=0
    else:
        cost+=1
    if btn5['text']=="5":
        cost+=0
    else:
        cost+=1
    if btn6['text']=="6":
        cost+=0
    else:
        cost+=1
    if btn7['text']=="7":
        cost+=0
    else:
        cost+=1
    if btn8['text']=="8":
        cost+=0
    else:
        cost+=1

    print('distance is',cost)

    


for x in range(10):
  Grid.columnconfigure(frame, x, weight=1)

for y in range(5):
  Grid.rowconfigure(frame, y, weight=1)


root.mainloop()
