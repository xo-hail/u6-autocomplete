import data

""" Split up the data into usable dictionaries. The brain of the program, if you will. """


def dictionary_assembly(words):
    word_bank = {}

    for word in words:
        if word in word_bank:
            continue

        word_bank[word]

    return word_bank

# dictionary = dictionary_assembly(data.data)

def clean_data(data):
    cleaned_data = []

    for phrase in data:
        words = data.split("", ",").lower()
        for word in words:
            cleaned_data.append(word)

    return cleaned_data

clean_Data = clean_data(data.data)
print(clean_Data)

def get_next_word(words, index):

    return words [index + 1]