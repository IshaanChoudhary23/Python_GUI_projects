from tkinter import *
first=second=operator=None


def get_digit(digit):
    current=result_label['text']
    new=current+ str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text='')


def get_result():
    global first,second,operator
    second=int(result_label['text'])
    if operator=="+":
        result_label.config(text=str(first+second))
    elif operator=="-":
        result_label.config(text=str(first - second))
    elif operator=="*":
        result_label.config(text=str(first * second))
    else:
        if second==0:
            result_label.config(text="error")
        else:
            result_label.config(text=str(first / second))

def get_operator(op):
    global first,operator
    first=int(result_label['text'])
    operator=op
    result_label.config(text='')








cal= Tk()

cal.title("Calculator")
cal.iconbitmap('calculator.ico')
cal.geometry("380x500")
cal.configure(background="black")


result_label= Label(cal,text="",bg="black",fg="white")
result_label.grid(row=0,column=0,columnspan=5,pady=(60,35),sticky='w')
result_label.config(font=('verdana',40,'bold'))


btn7=Button(text="7",bg="grey",fg="white",width=3,height=1,command=lambda : get_digit(7))     #  IF WE WNT TO PASS PARAMETER THEN WE USE LAMDA FUNCTIOM
btn7.grid(row=1,column=0)
btn7.config(font=('verdana',30,'bold'))

btn8=Button(text="8",bg="grey",fg="white",width=3,height=1,command=lambda : get_digit(8))
btn8.grid(row=1,column=1)
btn8.config(font=('verdana',30,'bold'))

btn9=Button(text="9",bg="grey",fg="white",width=3,height=1,command=lambda : get_digit(9))
btn9.grid(row=1,column=2)
btn9.config(font=('verdana',30,'bold'))

btn_add=Button(text="+",bg="grey",fg="white",width=3,height=1,command=lambda :get_operator('+'))
btn_add.grid(row=1,column=3)
btn_add.config(font=('verdana',30,'bold'))

btn4=Button(text="4",bg="grey",fg="white",width=3,height=1,command=lambda : get_digit(4))
btn4.grid(row=2,column=0)
btn4.config(font=('verdana',30,'bold'))

btn5=Button(text="5",bg="grey",fg="white",width=3,height=1,command=lambda : get_digit(5))
btn5.grid(row=2,column=1)
btn5.config(font=('verdana',30,'bold'))

btn6=Button(text="6",bg="grey",fg="white",width=3,height=1,command=lambda : get_digit(6))
btn6.grid(row=2,column=2)
btn6.config(font=('verdana',30,'bold'))

btn_sub=Button(text=" -",bg="grey",fg="white",width=3,height=1,command=lambda :get_operator('-'))
btn_sub.grid(row=2,column=3)
btn_sub.config(font=('verdana',30,'bold'))


btn1=Button(text="1",bg="grey",fg="white",width=3,height=1,command=lambda : get_digit(1))
btn1.grid(row=3,column=0)
btn1.config(font=('verdana',30,'bold'))


btn2=Button(text="2",bg="grey",fg="white",width=3,height=1,command=lambda : get_digit(2))
btn2.grid(row=3,column=1)
btn2.config(font=('verdana',30,'bold'))


btn3=Button(text="3",bg="grey",fg="white",width=3,height=1,command=lambda : get_digit(3))
btn3.grid(row=3,column=2)
btn3.config(font=('verdana',30,'bold'))


btn_div=Button(text="/",bg="grey",fg="white",width=3,height=1,command=lambda :get_operator('/'))
btn_div.grid(row=3,column=3)
btn_div.config(font=('verdana',30,'bold'))


btn_c=Button(text="C",bg="grey",fg="white",width=3,height=1,command=lambda :clear())
btn_c.grid(row=4,column=0)
btn_c.config(font=('verdana',30,'bold'))


btn0=Button(text="0",bg="grey",fg="white",width=3,height=1,command=lambda : get_digit('0'))
btn0.grid(row=4,column=1)
btn0.config(font=('verdana',30,'bold'))


btn_eq=Button(text="=",bg="grey",fg="white",width=3,height=1,command= get_result)    #   LAMDA IS NOT USED BECAUSE WE  NOT PASS PARAMETER
btn_eq.grid(row=4,column=2)
btn_eq.config(font=('verdana',30,'bold'))


btn_mul=Button(text="*",bg="grey",fg="white",width=3,height=1,command=lambda :get_operator('*'))
btn_mul.grid(row=4,column=3)
btn_mul.config(font=('verdana',30,'bold'))







cal.mainloop()

