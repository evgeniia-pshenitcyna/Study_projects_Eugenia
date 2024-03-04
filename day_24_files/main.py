# with open("my_file.txt", mode="w") as file:
#     file.write("I love my family, yoga, flowers and traveling.")
#/Users/e.pshenitcyna/Desktop/my_file.txt
PATH = "../../../Desktop/my_file.txt"

with open(PATH, mode="a") as file:
    file.write("\nI love my family, yoga, flowers and traveling.")

with open(PATH) as file:
    contents = file.read()
    print(contents)
# file.close() - no need to use it if there is "with"

# creating non existing file
with open(PATH, mode="w") as file:
    file.write("I am beautiful, smart and brave.")
