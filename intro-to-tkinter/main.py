from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=400)

window.config(padx=100, pady=80)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=100, pady=100)


# Button
def button_clicked():
    my_label.config(text=userInput.get())


my_button = Button(text="Click Me", command=button_clicked)
my_button.grid(column=1, row=1)

second_button = Button(text="Click Me", command=button_clicked)
second_button.grid(column=2, row=0)

userInput = Entry(width=10)
userInput.grid(column=3, row=2)

window.mainloop()
