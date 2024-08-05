from tkinter import *

window_21 = Tk()
window_21.geometry("1920x1080")
window_21.title("21")

def begin():
    print(submit_player.get)
    value = 1
    return value

submit_player = Button(window_21,
                       text="Submit Player",
                       font=("Arial", 20, "bold"),
                       fg="red", bg="black",
                       command=begin)
submit_player.pack()
window_21.mainloop()