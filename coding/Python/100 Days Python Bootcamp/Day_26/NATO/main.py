student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas as pd
student_data_frame = pd.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

nato_alphas = pd.read_csv('./nato_phonetic_alphabet.csv')

Nato_dict = {row.letter:row.code for (idx,row) in nato_alphas.iterrows()}

# print(Nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
usr_input = input('Enter a name please')
usr_list = [Nato_dict[v.upper()] for v in usr_input]
print(usr_list)
