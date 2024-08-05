import time
from tkinter import *


def collatz_conjecture(n):
    sequence = [n]

    while n != 0:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)

    return sequence


def start_collatz():
    try:
        n = int(inputted_value.get())
        collatz_sequence = collatz_conjecture(n)

        for i, value in enumerate(collatz_sequence):
            value_var.set("The {} value is {}".format(i + 1, value))
            c_window.update()
            time.sleep(1)
    except ValueError:
        value_var.set("Please enter a valid integer.")


c_window = Tk()
c_window.geometry("600x400")
c_window.title("Collatz Conjecture")

value_var = StringVar()

value = Label(c_window, textvariable=value_var, font=("Arial", 16), fg="red", bg="black")
value.pack(pady=20)

inputted_value = Entry(c_window, font=("Arial", 16), fg="red", bg="black")
inputted_value.pack(pady=10)

start_button = Button(c_window, text="Start Collatz Conjecture", command=start_collatz)
start_button.pack(pady=10)

c_window.mainloop()
