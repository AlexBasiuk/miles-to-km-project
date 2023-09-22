from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    klm_result_label.config(text=f"{km}")

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=300)
window.config(padx=20, pady=20)

#Lables widgets

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label (text="is equal to")
is_equal_label.grid(column=0, row=1)

klm_result_label = Label(text="0")
klm_result_label.grid(column=1, row=1)

klm_label = Label(text="Km")
klm_label.grid(column=2, row=1)

culculate_button = Button(text="Get result", command=miles_to_km)
culculate_button.grid(column=1, row=2)

window.mainloop()