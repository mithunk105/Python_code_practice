REPLACE_IDENTIFIER = "[name]"

with open("./Input/Names/invited_names.txt") as receiver:
    names = receiver.readlines()
    with open("./Input/Letters/starting_letter.txt") as letter:
        content = letter.read()
        for mail_name in names:
            name = mail_name.strip()
            new_content = content.replace(REPLACE_IDENTIFIER, name)
            with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as output:
                output.write(new_content)

# Note - Check the path before run this code, it uses the relative path to read and write the file.
