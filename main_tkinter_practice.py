from tkinter import *

window = Tk()
window.title("TKINTER GUI PROGRAM")
window.minsize(width=500, height=500)

my_lable = Label(text="This is my lable", font=("Arial", 24))
my_lable.pack()


def when_button_clicked():
    print("Button clicked")
    my_lable["text"] = input.get()


button = Button(text="Click Me", command=when_button_clicked)
button.pack()


# Entry
input = Entry(width=50)
input.pack()
print(input.get())





















window.mainloop()