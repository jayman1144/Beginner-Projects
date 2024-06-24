import time
from tkinter import *

def inp():
        while True:
            n = value_var.get()
            count = 2
            while n!=0:
                if n % 2 == 0:
                    n = n/2
                    time.sleep(3)
                    value_var.set("The " + str(count) + " value is " + str(n))
                    c_window.update()
                    count += 1


                else:
                    n = (3*n)+1
                    time.sleep(3)
                    value_var.set("The " + str(count) + " value is " + str(n))
                    c_window.update()
                    count += 1



c_window = Tk()
c_window.geometry("1920x1080")
c_window.title("Collatz Conjecture")



value_var = StringVar()

value = Label(c_window,
              font=("Arial", 30),
              fg="red",
              bg="black",
              )

inputted_value = Entry(c_window,
                       font = ("Arial",30),
                       fg = "red",
                       bg = "black",
                       )

inputted_value.pack(side = LEFT)
value.pack(side = RIGHT)

c_window.mainloop()

