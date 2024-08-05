import time
from tkinter import *

collatz_window = Tk()
collatz_window.geometry("1920x1080")
collatz_window.title("Collatz Conjecture")

def save():
    try:
        saved_value = int(initial_value.get())
        check.config(text="That is a number")
        count = 0
        collatz_list = []

        while count <15:
            if saved_value % 2==0:
                saved_value = saved_value /2
                collatz_list.append(saved_value)


            else:
                saved_value = (3* saved_value) + 1
                collatz_list.append(saved_value)

            count +=1

        output.config(text=collatz_list)



    except ValueError:
        check.config(text="That is not a number")

check = Label(collatz_window,
                    font=("Arial",20,"bold"),
                    fg = "blue",bg ="black",
                    text="")


initial_value = Entry(collatz_window,
                      font=("Arial",20,"bold"),
                      fg="red",bg="black",)

enter_button = Button(collatz_window,
                      text="Submit value",
                      font=("Arial",20,"bold"),
                      fg="red",bg="black",
                      activeforeground="red", activebackground="black",
                      command=save)

output = Label(collatz_window,
               text="",
               font=("Arial", 20, "bold"),
               fg="purple", bg="black")

check.pack(pady=90)
initial_value.pack(pady=20)
enter_button.pack(pady=50)
output.pack(pady=40)

collatz_window.mainloop()
