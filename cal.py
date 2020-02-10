from tkinter import *  
op = ""
def press(num): 
    global op
    op = op + str(num)
    equation.set(op)

def equalpress():
    try:
        global op
        total = str(eval(op))
        equation.set(total)
        op = ""
    except:
        equation.set(" error ")
        op = ""


def clear():
    global op
    op = ""
    equation.set("")

abc = Tk()
abc.configure(background="light grey")
abc.title("Calculator")
abc.geometry("350x400")
equation = StringVar()
op_field = Entry(abc,font=("arial",30,"bold"),textvariable=equation)
op_field.grid(columnspan=70,ipadx=70)
equation.set('enter the operand')

button1 = Button(abc, text=' 1 ', fg='black', bg='white', command=lambda: press(1), height=5, width=10)
button1.grid(row=2, column=0)

button2 = Button(abc, text=' 2 ', fg='black', bg='white', command=lambda: press(2), height=5, width=10)
button2.grid(row=2, column=1)

button3 = Button(abc, text=' 3 ', fg='black', bg='white', command=lambda: press(3), height=5, width=10)
button3.grid(row=2, column=2)

button4 = Button(abc, text=' 4 ', fg='black', bg='white', command=lambda: press(4), height=5, width=10)
button4.grid(row=3, column=0)

button5 = Button(abc, text=' 5 ', fg='black', bg='white', command=lambda: press(5), height=5, width=10)
button5.grid(row=3, column=1)

button6 = Button(abc, text=' 6 ', fg='black', bg='white', command=lambda: press(6), height=5, width=10)
button6.grid(row=3, column=2)

button7 = Button(abc, text=' 7 ', fg='black', bg='white', command=lambda: press(7), height=5, width=10)
button7.grid(row=4, column=0)

button8 = Button(abc, text=' 8 ', fg='black', bg='white', command=lambda: press(8), height=5, width=10)
button8.grid(row=4, column=1)

button9 = Button(abc, text=' 9 ', fg='black', bg='white', command=lambda: press(9), height=5, width=10)
button9.grid(row=4, column=2)

button0 = Button(abc, text=' 0 ', fg='black', bg='white', command=lambda: press(0), height=5, width=10)
button0.grid(row=5, column=0)

plus = Button(abc, text=' + ', fg='black', bg='white', command=lambda: press("+"), height=5, width=10)
plus.grid(row=2, column=3)

minus = Button(abc, text=' - ', fg='black', bg='white', command=lambda: press("-"), height=5, width=10)
minus.grid(row=3, column=3)

 multiply = Button(abc, text=' * ', fg='black', bg='white', command=lambda: press("*"), height=5, width=10)
multiply.grid(row=4, column=3)

divide = Button(abc, text=' / ', fg='black', bg='white', command=lambda: press("/"), height=5, width=10)
divide.grid(row=5, column=3)

equal = Button(abc, text=' = ', fg='black', bg='white', command=equalpress, height=5, width=10)
equal.grid(row=5, column=2)

clear = Button(abc, text='Clear', fg='black', bg='white', command=clear, height=5, width=10)
clear.grid(row=5, column='1')
  
abc.mainloop()
