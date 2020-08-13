from tkinter import *
import math

def btn_Click(numbers):
    global operator
    operator=operator + str(numbers)
    text_input.set(operator)

def btnclrDisplay():
    global operator
    operator=""
    text_input.set("") 

def delete():
    global operator
    text_input.set(text_input.get() [:-1])     

def btn_Equ():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=""






cal=Tk()
cal.title("calculator")
cal.geometry("451x621")
cal.resizable(0,0)
operator=""
text_input = StringVar()
cal.config(background="skyblue")

textDisplay=Entry(cal,font=("arial",20,'bold'), textvariable=text_input ,bd=50,insertwidth=4,bg="powder blue",justify="right").grid(columnspan=5)
btnclr=Button(cal,padx=16,bd=20,bg="purple",fg="black",font=("arial",20,'bold'),text="C",command=btnclrDisplay).grid(row=1,column=0)
PER=Button(cal,padx=16,bd=20,bg="purple",fg="black",font=("arial",20,'bold'),text="%",command=lambda:btn_Click("%")).grid(row=1,column=1)
DEL=Button(cal,padx=16,bd=20,bg="purple",fg="black",font=("arial",20,'bold'),text="<",command=delete).grid(row=1,column=2)
Div=Button(cal,padx=16,bd=23,fg="black",bg="purple",font=("arial",20,'bold'),text="/",command=lambda:btn_Click("/")).grid(row=1,column=3)
btn7=Button(cal,padx=16,bd=22,bg="blue",fg="black",font=("arial",20,'bold'),text="7",command=lambda:btn_Click(7)).grid(row=2,column=0)
btn8=Button(cal,padx=16,bd=23,bg="blue",fg="black",font=("arial",20,'bold'),text="8",command=lambda:btn_Click(8)).grid(row=2,column=1)
btn9=Button(cal,padx=16,bd=22,bg="blue",fg="black",font=("arial",20,'bold'),text="9",command=lambda:btn_Click(9)).grid(row=2,column=2)
mult=Button(cal,padx=16,bd=21,bg="purple",fg="black",font=("arial",20,'bold'),text="x",command=lambda:btn_Click("*")).grid(row=2,column=3)
btn4=Button(cal,padx=16,bd=22,bg="blue",fg="black",font=("arial",20,'bold'),text="4",command=lambda:btn_Click(4)).grid(row=3,column=0)
btn5=Button(cal,padx=16,bd=23,bg="blue",fg="black",font=("arial",20,'bold'),text="5",command=lambda:btn_Click(5)).grid(row=3,column=1)
btn6=Button(cal,padx=16,bd=22,bg="blue",fg="black",font=("arial",20,'bold'),text="6",command=lambda:btn_Click(6)).grid(row=3,column=2)
sub=Button(cal,padx=16,bd=22,bg="purple",fg="black",font=("arial",20,'bold'),text="-",command=lambda:btn_Click("-")).grid(row=3,column=3)
btn1=Button(cal,padx=16,bd=22,bg="blue",fg="black",font=("arial",20,'bold'),text="1",command=lambda:btn_Click(1)).grid(row=4,column=0)
btn2=Button(cal,padx=16,bd=23,bg="blue",fg="black",font=("arial",20,'bold'),text="2",command=lambda:btn_Click(2)).grid(row=4,column=1)
btn3=Button(cal,padx=16,bd=22,bg="blue",fg="black",font=("arial",20,'bold'),text="3",command=lambda:btn_Click(3)).grid(row=4,column=2)
add=Button(cal,padx=16,bd=21,bg="purple",fg="black",font=("arial",20,'bold'),text="+",command=lambda:btn_Click("+")).grid(row=4,column=3)
dowmbtn=Button(cal,padx=16,bd=21,bg="purple",fg="black",font=("arial",20,'bold'),text="**",command=lambda:btn_Click("**")).grid(row=5,column=0)
btn0=Button(cal,padx=16,bd=23,bg="purple",fg="black",font=("arial",20,'bold'),text="0",command=lambda:btn_Click(0)).grid(row=5,column=1)
deci=Button(cal,padx=16,bd=24,bg="purple",fg="black",font=("arial",20,'bold'),text=".",command=lambda:btn_Click(".")).grid(row=5,column=2)
equal=Button(cal,padx=16,bd=22.5,bg="purple",fg="black",font=("arial",20,'bold'),text="=",command=btn_Equ).grid(row=5,column=3)

cal.mainloop()