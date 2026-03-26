from tkinter import *

first_number = second_number = operator = None

def get_digit(digit):
    current = result_label['text']
    new = str(current) + str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text="")

def get_operator(op):
    global first_number,operator
    first_number = int(result_label['text'])
    operator = op
    result_label.config(text="")

def result():
    global first_number,operator, second_number
    second_number = int(result_label['text'])
    if operator == '+':
        result_label.config(text=str(first_number + second_number))
    elif operator == '-':
        result_label.config(text=str(first_number - second_number))
    elif operator == '*':
        result_label.config(text=str(first_number * second_number))
    else:
        if second_number == 0:
            result_label.config(text="Error")
        else:
            result_label.config(text=str(round(first_number / second_number)))

root = Tk()
root.geometry("275x285")
root.title("Calculator")
root.resizable(0,0)
root.configure(background="black")

result_label = Label(root,text='',bg="black",fg="white")
result_label.grid(row=0,column=0,columnspan=5,pady=(50,25),sticky='w')
result_label.config(font=("verdana",30,"bold"))

btn7 = Button(root,text="7",bg="#00a65a",fg="white",width=5,height=1,command=lambda :get_digit(7))
btn7.grid(row=1,column=0)
btn7.config(font=("verdana",14))

btn8 = Button(root,text="8",bg="#00a65a",fg="white",width=5,height=1,command=lambda :get_digit(8))
btn8.grid(row=1,column=1)
btn8.config(font=("verdana",14))

btn9 = Button(root,text="9",bg="#00a65a",fg="white",width=5,height=1,command=lambda :get_digit(9))
btn9.grid(row=1,column=2)
btn9.config(font=("verdana",14))

btnP = Button(root,text="+",bg="#00a65a",fg="white",width=5,height=1,command=lambda :get_operator('+'))
btnP.grid(row=1,column=3)
btnP.config(font=("verdana",14))

btn4 = Button(root,text="4",bg="#00a65a",fg="white",width=5,height=1,command=lambda :get_digit(4))
btn4.grid(row=2,column=0)
btn4.config(font=("verdana",14))

btn5 = Button(root,text="5",bg="#00a65a",fg="white",width=5,height=1,command=lambda :get_digit(5))
btn5.grid(row=2,column=1)
btn5.config(font=("verdana",14))

btn6 = Button(root,text="6",bg="#00a65a",fg="white",width=5,height=1,command=lambda :get_digit(6))
btn6.grid(row=2,column=2)
btn6.config(font=("verdana",14))

btnN = Button(root,text="-",bg="#00a65a",fg="white",width=5,height=1,command=lambda :get_operator('-'))
btnN.grid(row=2,column=3)
btnN.config(font=("verdana",14))

btn1 = Button(root,text="1",bg="#00a65a",fg="white",width=5,height=1,command=lambda :get_digit(1))
btn1.grid(row=3,column=0)
btn1.config(font=("verdana",14))

btn2 = Button(root,text="2",bg="#00a65a",fg="white",width=5,height=1,command=lambda :get_digit(2))
btn2.grid(row=3,column=1)
btn2.config(font=("verdana",14))

btn3 = Button(root,text="3",bg="#00a65a",fg="white",width=5,height=1,command=lambda :get_digit(3))
btn3.grid(row=3,column=2)
btn3.config(font=("verdana",14))

btnM = Button(root,text="*",bg="#00a65a",fg="white",width=5,height=1,command=lambda :get_operator('*'))
btnM.grid(row=3,column=3)
btnM.config(font=("verdana",14))

btnC = Button(root,text="C",bg="#00a65a",fg="white",width=5,height=1,command=clear)
btnC.grid(row=4,column=0)
btnC.config(font=("verdana",14))

btn0 = Button(root,text="0",bg="#00a65a",fg="white",width=5,height=1,command=lambda :get_digit(0))
btn0.grid(row=4,column=1)
btn0.config(font=("verdana",14))

btnE = Button(root,text="=",bg="#00a65a",fg="white",width=5,height=1,command=result)
btnE.grid(row=4,column=2)
btnE.config(font=("verdana",14))

btnD = Button(root,text="/",bg="#00a65a",fg="white",width=5,height=1,command=lambda :get_operator('/'))
btnD.grid(row=4,column=3)
btnD.config(font=("verdana",14))

root.mainloop()