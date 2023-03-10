import string
from functools import reduce


def second_program(input_file, dictionary_file):
    """
    Reads the given input file and dictionary file, counts the occurrences of each word in the input file, and writes
    the results to a new file.
    :param input_file: A string representing the file path of the input file.
    :param dictionary_file: A string representing the file path of the dictionary file.
    :return: A string representing the file path of the output file.
    """
    with open(input_file, 'r') as text_file, open(dictionary_file, 'r') as dict_file:
        text = text_file.read()
        dictionary = eval(dict_file.read())
    clean_words = map(lambda word: word.lower().strip(string.punctuation), text.split())
    clean_words = filter(lambda word: word.isalpha(), clean_words)
    word_counts = reduce(lambda counts, word: counts.update({word: counts.get(word, 0) + 1}) or counts, clean_words, {})
    word_list = map(lambda word: (word, word_counts[word], dictionary.get(word, {})), word_counts)
    word_list = sorted(word_list, key=lambda x: (-x[1], x[0]))
    with open('words.txt', 'w') as words_file:
        words_file.write(str(word_list))
    return repr('words.txt')


# Running the program:
second_program('text.txt', 'dictionary.txt')