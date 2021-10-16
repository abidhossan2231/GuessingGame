import tkinter as tk
from functools import partial
from random import randint
from tkinter import messagebox

def call_result(label_result, n1):
    num1 = (n1.get())
    num2 = randint(1, 10)
    result = num2

    rn = randint(1, 10)
    if num1 == rn:
        messagebox.showinfo("Hey Dear", "Your guessing number is correct. ")
    else:
        label_result.config(text="Random Number is : %d" % result)
        messagebox.showwarning("Hey Dear", "Your guessing number is wrong.")

root = tk.Tk()
root.geometry('400x200+100+200')
c = tk.Canvas(root, bg="pink", height="200", width=200+100+200)
root.title('Guessing Number Game')
number1 = tk.IntVar()


labelNum = tk.Label(root, text="Input your guessing number between 1 to 10 ").place(x=70, y=15)
labelNum1 = tk.Label(root, text="Guess Number :").place(x=80, y=65)
labelNum2 = tk.Label(root, text="abidhossan2231").place(x=25, y=150)
labelNum3 = tk.Label(root, text="Using language Python").place(x=5, y=170)
labelResult = tk.Label(root)
labelResult.place(x=265, y=170)

entryNum1 = tk.Entry(root, textvariable=number1).place(x=180, y=65)

call_result = partial(call_result, labelResult, number1)
buttonCal = tk.Button(root, text="Check", command=call_result, activebackground="pink", activeforeground="blue").place(x=180, y=130)
c.pack()
root.mainloop()
