import pandas

nato_alpha = pandas.read_csv("nato_phonetic_alphabet.csv")
alpha_dict = {row.letter: row.code for (index, row) in nato_alpha.iterrows()}
user_input = input("What's the text?: ")
output_list = [alpha_dict[char] for char in user_input]

print(output_list)
