# Placeholder for the name to be replaced in the letter
PLACE = "[name]"

# Read the list of names from the input file
with open("./Input/Names/invited_names.txt") as names:
    name_list = names.readlines()

# Read the content of the starting letter
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()

    # Iterate through each name in the list
    for name in name_list:
        name = name.strip()  # Remove any leading/trailing whitespace

        # Replace the placeholder with the current name
        new_letter = letter.replace(PLACE, name)

        # Write the personalized letter to a new output file
        with open(f"./Output/ReadyToSend/letter_{name}.txt", mode="w") as name_letter:
            name_letter.write(new_letter)
