import pandas

# create pandas dataframe from the csv file
df = pandas.read_csv("nato_phonetic_alphabet.csv")
# make a dictionary of letter:code pairs from dataframe rows
nato_alphabet = {row.letter: row.code for (index, row) in df.iterrows()}

word = input("Enter a word: ").upper()

# Make list of the codes for each letter in the letter list
nato_list = [nato_alphabet[letter] for letter in word]
print(nato_list)
