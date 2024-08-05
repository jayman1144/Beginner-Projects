from tkinter import *
window = Tk()
window.geometry("500x500")



value = Label(window,
              text ="Hello",
              font=("Arial", 30,"bold"),
              fg="red",
              bg="black")

inputted_value = Entry(window,
                       font = ("Arial",30,"bold"),
                       fg = "red",
                       bg = "black")

window.mainloop()

inputted_value.pack()
value.pack()