# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# student_data_frame = pd.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


import pandas as pd

is_on = True
while is_on:
    #TODO 1. Create a dictionary in this format:
    data = pd.read_csv("nato_phonetic_alphabet.csv")

    nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

    #TODO 2. Create a list of the phonetic code words from a word that the user inputs.

    user_name = list(input("Enter your name\n").upper())

    try:
        result = [nato_dict[letter] for letter in user_name]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(result)
        is_on = False
