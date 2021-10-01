from tkinter import *
window = Tk()
def from_kg():
    pound = float(ent2_value.get())*2.20462
    ounce = float(ent2_value.get())*35.274
    gram = float(ent2_value.get())*1000
    x1.delete("1.0", END)
    x1.insert(END, pound)
    x2.delete("1.0", END)
    x2.insert(END, ounce)
    x3.delete("1.0",END)
    x3.insert(END, gram)

ent1 = Label(window, text="Input the weight in KG")
ent2_value = StringVar()
ent2 = Entry(window, textvariable=ent2_value)
ent3 = Label(window, text="Pound")
ent4 = Label(window, text="Ounce")
ent5 = Label(window, text="Gram")

x1 = Text(window, height=5, width=30)
x2 = Text(window, height=5, width=30)
x3 = Text(window, height=5, width=30)

but1 = Button(window, text="Convert It!", command=from_kg)

ent1.grid(row=0, column=0)
ent2.grid(row=0, column=1)
ent3.grid(row=1, column=0)
ent4.grid(row=1, column=1)
ent5.grid(row=1, column=2)
x1.grid(row=2, column=0)
x2.grid(row=2, column=1)
x3.grid(row=2, column=2)
but1.grid(row=0, column=2)

window.mainloop()