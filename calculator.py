# Built a simple calculator with tkinter in python
# Spiros Kavvathas

from tkinter import *
import math

root = Tk()
root.title("Simple Calculator")


box = Entry(root, width=30, borderwidth=5)
box.grid(row=0, column=0, columnspan=4)


def press_button(number):
    current = box.get()
    box.delete(0, END)
    box.insert(0, str(current) + str(number))


# Clear the entry box
def press_clear():
    box.delete(0, END)


def press(symbol):
    first_number = box.get()
    global f_num
    global symboli
    symboli = str(symbol)
    f_num = float(first_number)
    box.delete(0, END)


# add, division , multiplication, subtraction
def press_equal():
    second_number = box.get()
    if symboli == "+":
        num = float(second_number) + f_num
    elif symboli == "-":
        num = float(second_number) - f_num
    elif symboli == "*":
        num = float(second_number)*f_num
    elif symboli == "/":
        num = f_num/float(second_number)

    box.delete(0, END)
    box.insert(0, str(num))


def press_log():
    box.insert(0, math.log(float(box.get())))


# x^2
def press_x2():
    num1 = box.get()
    box.insert(0, float(num1)*float(num1))


def press_sqrt():
    box.insert(0, math.sqrt(float(box.get())))


def press_factorial():
    box.insert(0, math.factorial(float(box.get())))


def press_ex():
    box.insert(0, math.exp(float(box.get())))


button0 = Button(root, text="0", bg="white", width=6, height=3, borderwidth=2, command=lambda: press_button(0))
button1 = Button(root, text="1", bg="white", width=6, height=3, borderwidth=2, command=lambda: press_button(1))
button2 = Button(root, text="2", bg="white", width=6, height=3, borderwidth=2, command=lambda: press_button(2))
button3 = Button(root, text="3", bg="white", width=6, height=3, borderwidth=2, command=lambda: press_button(3))
button4 = Button(root, text="4", bg="white", width=6, height=3, borderwidth=2, command=lambda: press_button(4))
button5 = Button(root, text="5", bg="white", width=6, height=3, borderwidth=2, command=lambda: press_button(5))
button6 = Button(root, text="6", bg="white", width=6, height=3, borderwidth=2, command=lambda: press_button(6))
button7 = Button(root, text="7", bg="white", width=6, height=3, borderwidth=2, command=lambda: press_button(7))
button8 = Button(root, text="8", bg="white", width=6, height=3, borderwidth=2, command=lambda: press_button(8))
button9 = Button(root, text="9", bg="white", width=6, height=3, borderwidth=2, command=lambda: press_button(9))
button_add = Button(root, text="+", bg="bisque2", width=6, height=3, borderwidth=2, command=lambda: press("+"))
button_minus = Button(root, text="-", bg="bisque2", width=6, height=3, borderwidth=2, command=lambda: press("-"))
button_mult = Button(root, text="*", bg="bisque2", width=6, height=3, borderwidth=2, command=lambda: press("*"))
button_divide = Button(root, text="/", bg="bisque2", width=6, height=3, borderwidth=2, command=lambda: press("/"))
button_comma = Button(root, text=",", bg="bisque2", width=6, height=3, borderwidth=2, command=lambda: press_button("."))
button_equal = Button(root, text="=", bg="cyan", width=6, height=3, borderwidth=2, command=press_equal)
button_clear = Button(root, text="Clear", bg="salmon", width=30, height=4, borderwidth=2, command=press_clear)
button_log = Button(root, text="log", bg="bisque2", width=6, height=3, borderwidth=2, command=press_log)
button_x2 = Button(root, text="x^2", bg="bisque2", width=6, height=3, borderwidth=2, command=press_x2)
button_sqrt = Button(root, text="sqrt", bg="bisque2", width=6, height=3, borderwidth=2, command=press_sqrt)
button_factorial = Button(root, text="n!", bg="bisque2", width=6, height=3, borderwidth=2, command=press_factorial)
button_ex = Button(root, text="e^x", bg="bisque2", width=6, height=4, borderwidth=2, command=press_ex)

button0.grid(row=4, column=1)
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
button_add.grid(row=1, column=3)
button_minus.grid(row=2, column=3)
button_mult.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_comma.grid(row=4, column=0)
button_equal.grid(row=4, column=2)
button_clear.grid(row=5, column=0, columnspan=4)
button_log.grid(row=1, column=4)
button_x2.grid(row=2, column=4)
button_sqrt.grid(row=3, column=4)
button_factorial.grid(row=4, column=4)
button_ex.grid(row=5, column=4)

root.mainloop()
