#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#f = open("demofile.txt", "r")
#print(f.readlines())

with open("Input/Letters/starting_letter.txt") as file:
    letter_text = file.read()
    print(letter_text)

with open("Input/Names/invited_names.txt") as file:
    names_list = []
    for n in range(1, 8):
        name = file.readlines(n)
        names_list.append(str(name).strip("['\\n']"))
    print(names_list)

for name in names_list:
    letter = letter_text.replace("[name]", name)
    txt = "letter_" + name + ".txt"
    with open(f"Output/ReadyToSend/{txt}", mode="w") as file:
        file.write(letter)
