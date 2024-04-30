from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=250)

window.config(padx=100, pady=100)

userInput = Entry(width=20)
userInput.grid(column=0, row=0)

# Label with "Miles" text
label1 = Label(text="Miles", font=("Arial", 15, "normal"))
label1.grid(column=1, row=0)

# Label with "is equal to" text
label2 = Label(text="is equal to", font=("Arial", 15, "normal"))
label2.grid(column=0, row=1)

# Label with km value
km_label = Label(text=0, font=("Arial", 15, "normal"))
km_label.grid(column=0, row=2)

# Label with "Km" text
label3 = Label(text="Km", font=("Arial", 15, "normal"))
label3.grid(column=1,row=2)

# Convert Function Formula = (km = mile * 1.609344)
def convert():
    km = round(int(userInput.get()) * 1.609344, 2)
    km_label.config(text=km)


button = Button(text="Convert", command=convert)
button.grid(column=0, row=3)

window.mainloop()
