# with open("my_file.txt", mode="w") as file:
#     file.write("I love my family, yoga, flowers and traveling.")

with open("my_file.txt", mode="a") as file:
    file.write("\nI love my family, yoga, flowers and traveling.")

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
# file.close() - no need to use it if there is "with"

# creating non existing file
with open("new_file.txt", mode="w") as file:
    file.write("I am beautiful, smart and brave.")