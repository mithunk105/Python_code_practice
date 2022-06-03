from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=100, height=50)
window.config(padx=20, pady=20)


equal_lable = Label(text="is equal to", font=("Arial", 10, "normal"))
equal_lable.grid(row=2, column=0)

cal_button = Button(text="Calculate")
cal_button.grid(row=3, column=1)

km_lable = Label(text="Km", font=("Arial", 10, "normal"))
km_lable.grid(row=2, column=2)

value_lable = Label(text=f"{0}", font=("Arial", 10, "normal"))
value_lable.grid(row=2, column=1)

miles_lable = Label(text="   Miles", font=("Arial", 10, "normal"))
miles_lable.grid(row=1, column=2)

miles_entry = Entry(width=8)
miles_entry.grid(row=1, column=1)


def calculate_kms():
    value_lable.config(text=round(1.609 * int(miles_entry.get())))


cal_button.config(command=calculate_kms)


window.mainloop()
