import string


def program_two(text_file_name, dictionary_file_name):
    with open(text_file_name, 'r') as text_file, open(dictionary_file_name, 'r') as dict_file:
        text_str = text_file.read()
        dictionary = eval(dict_file.read())
    words = text_str.split()
    clean_words = []
    for word in words:
        clean_word = word.lower().strip(string.punctuation)
        if clean_word.isalpha():
            clean_words.append(clean_word)

    word_count = {}
    for word in clean_words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    word_list = []
    for word, count in word_count.items():
        categories = dictionary.get(word, {})
        word_list.append((word, count, categories))
    word_list.sort(key=lambda x: (x[0]))
    word_list.sort(key=lambda x: (-x[1]))
    with open('words.txt', 'w') as words_file:
        words_file.write(str(word_list))
    return repr('words.txt')

from functools import reduce

def program_two(file1, file2):
    with open(file1, 'r') as text_file, open(file2, 'r') as dict_file:
        text = text_file.read()
        dictionary = eval(dict_file.read())
    # Use map to apply the `lower` and `strip` functions to each word in the text
    clean_words = map(lambda word: word.lower().strip(string.punctuation), text.split())
    # Use filter to remove any non-alphabetic words
    clean_words = filter(lambda word: word.isalpha(), clean_words)

    # Use reduce to count the occurrences of each word
    word_count = reduce(lambda counts, word: counts.update({word: counts.get(word, 0) + 1}) or counts, clean_words, {})

    # Use map to add categories from the dictionary to each word
    word_list = map(lambda word: (word, word_count[word], dictionary.get(word, {})), word_count)
    # Use sorted to sort the list by word and then by count
    word_list = sorted(word_list, key=lambda x: (x[0], -x[1]))

    with open('words.txt','w') as words_file:
        words_file.write(str(word_list))
    return repr('words.txt')


print(program_two('text.txt', 'dictionary.txt'))
