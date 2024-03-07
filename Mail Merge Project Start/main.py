with open("Input/Letters/starting_letter.txt") as file:
    letter_text = file.read()
    print(letter_text)

with open("Input/Names/invited_names.txt") as file:
    names_list = []
    for n in range(1, 9):
        name = file.readlines(n)
        names_list.append(str(name).strip("[\\\n\\n']"))
    print(names_list)

for name in names_list:
    name = name.strip('""')
    letter = letter_text.replace("[name]", name)
    txt = "letter_" + name + ".txt"
    with open(f"Output/ReadyToSend/{txt}", mode="w") as file:
        file.write(letter)
