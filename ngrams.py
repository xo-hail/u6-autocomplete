import data

""" Split up the data into usable dictionaries. The brain of the program, if you will. """


""" Returns a bigram dictionary. """

def dictionary_assembly(words):
    word_bank = {}

    if word not in word_bank:
            word_bank[word] = []

    return word_bank

""" In progress. Have yet to understand this block of code. """

def get_next_word(words, index):

    return words [index + 1]

def data_prep(data):
    words_list = []

    for i in range(len(data)):
        words = data[i].split()

        for word in words:
            words_list.append(word)

    return words_list

prepped_Data = data_prep(data.data)
print(prepped_Data)