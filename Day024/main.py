PLACEHOLDER = "[name],"

with open("./Input/Names/invited_names.txt", mode="r") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt", mode="r") as letter_file:
    letter = letter_file.read()

for name in names:
    name = name.strip()
    message = letter.replace(PLACEHOLDER, f"{name},")

    file_name = f"letter_for_{name}.docx"
    with open(f"./Output/ReadyToSend/{file_name}", mode="w") as output:
        output.write(message)
