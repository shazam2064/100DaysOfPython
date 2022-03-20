from tkinter import *


def button_clicked():
    print(".F.U.")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My Not First SIT Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

#Label
my_label = Label(text="Joe Mama Fat", font=("Arial", 24, "bold"))
my_label.config(text="Joe Mama Fat")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

#Button
button = Button(text="Click To Die", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="Useless Button")
new_button.grid(column=2, row=0)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)









window.mainloop()