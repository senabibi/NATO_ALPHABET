"""student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass
"""
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas
data=pandas.read_csv(r"C:\Users\SENA\Downloads\NATO-alphabet-start\NATO-alphabet-start\nato_phonetic_alphabet.csv")
print(data.to_dict())
new_dict={row.letter:row.code for (index, row) in data.iterrows()}
print(new_dict)

word=input("Enter the word:").upper()

last_dict=[new_dict[letter] for letter in word]
print(last_dict)


