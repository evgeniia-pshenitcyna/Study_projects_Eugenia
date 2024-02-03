import tkinter


def button_clicked():
    print("I've got clicked.")
    number = user_input.get()
    number_km = int(number)*1.60934
    start_number.config(text=number_km)


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=450, height=250)
window.config(padx=20, pady=20)

# Labels
equal_label = tkinter.Label(text="is equal to", font=("Arial", 20))
equal_label.grid(column=0, row=1)
equal_label.config(padx=40, pady=20)

miles_label = tkinter.Label(text="Miles", font=("Arial", 20))
miles_label.grid(column=2, row=0)
miles_label.config(padx=20, pady=20)

km_label = tkinter.Label(text="Km", font=("Arial", 20))
km_label.grid(column=2, row=1)
km_label.config(padx=40, pady=20)

start_number = tkinter.Label(text="0", font=("Arial", 20))
start_number.grid(column=1, row=1)
start_number.config(padx=20, pady=20)

# Button
calculate_button = tkinter.Button(text="Calculate", command=button_clicked)
calculate_button.grid(column=1, row=2)

# Entry
user_input = tkinter.Entry(width=10)
print(user_input.get())
user_input.grid(column=1, row=0)

window.mainloop()
