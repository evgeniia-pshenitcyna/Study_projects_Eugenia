import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New text"
my_label.config(text="Cat")


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


# Button
my_button = tkinter.Button(text="Click me", command=button_clicked)
my_button.pack()

# Entry
input = tkinter.Entry(width=10)
input.pack()

window.mainloop()
