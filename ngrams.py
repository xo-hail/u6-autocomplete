import data

""" Split up the data into usable dictionaries. The brain of the program, if you will. """

raw_Data = data.data

""" Returns a bigram dictionary. """

def dictionary_assembly(raw_data):
    prepped_data = data_prep(raw_data)
    word_bank = {}

    for word in prepped_data:
        if word not in word_bank:
                word_bank[word] = []

    return word_bank

""" In progress. Have yet to understand this block of code. """

def get_next_word(words, index):

    return words [index + 1]

def data_prep(raw_data):
    words_list = []

    for i in range(len(raw_data)):
        words = raw_data[i].split()

        for word in words:
            words_list.append(word)

    return words_list


dictionary = dictionary_assembly(raw_Data)
print(dictionary)
