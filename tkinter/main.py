import tkinter


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=10, pady=10)

# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)

my_label["text"] = "New text"
my_label.config(text="Cat")

# Button
my_button = tkinter.Button(text="Click me", command=button_clicked)
my_button.grid(column=1, row=1)

# Entry
input = tkinter.Entry(width=10)
input.grid(column=3, row=2)

# Button
new_button = tkinter.Button(text="New button", command=button_clicked)
new_button.grid(column=2, row=0)

window.mainloop()
