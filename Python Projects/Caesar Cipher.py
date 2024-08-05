from tkinter import *

cipher = Tk()
cipher.geometry("1920x1080")
cipher.title("Caesar Cipher")
def scramble():
    pre_scrambled = inputted.get()
    post_scrambled = []
    count = 0

    while count<len(pre_scrambled):
        ac = ord(pre_scrambled[count])
        ac +=3
        count+=1

        post_scrambled.append(chr(ac))

    output.config(text=post_scrambled)
    display.config(text="This is the encoded message")


inputted = Entry(cipher,
                 font=("Arial",20,"bold"),
                 fg="blue",bg="orange")

save = Button(cipher,
              text="Submit words",
              font=("Arial", 20, "bold"),
              fg="blue", bg="orange",
              command=scramble)

display = Label(cipher,
                font=("Arial", 10, "bold"),
                fg="blue")

output = Label(cipher,
               font=("Arial", 20, "bold"),
               fg="green", bg="orange")


inputted.pack(pady=20)
save.pack(pady=30)
display.pack()
output.pack()

cipher.mainloop()