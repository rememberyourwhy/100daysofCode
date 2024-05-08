# Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# open text file & read
with open("Input/Letters/starting_letter.txt", mode="r") as sample_letter_file:
    sample_letter = sample_letter_file.read()

# split
with open("Input/Names/invited_names.txt", mode="r") as invited_names:
    name_str = invited_names.read()
    name_list = name_str.split("\n")

# check for bold text 
for name in name_list:
    temp_letter = sample_letter
    temp_letter = temp_letter.replace("[name]", name)
    path = f"Output/ReadyToSend/letter_for_{name}.txt"
    with open(path, mode="w") as finished_output:
        finished_output.write(temp_letter)
