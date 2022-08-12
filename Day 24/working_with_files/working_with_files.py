# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

with open("my_file.txt", mode="w") as file:
    file.write("New text.")

# modes: "r" read only
# "a" : append only
# "w" : write