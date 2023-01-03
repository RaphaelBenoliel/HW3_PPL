from functools import reduce


def program_one(file1, file2, file3, file4):
    f = open(file1, "r")
    file1_word = f.read().split()
    f = open(file2, "r")
    file2_word = f.read().split()
    f = open(file3, "r")
    file3_word = f.read().split()
    file3_word = list(map(lambda x: x.lower(), file3_word))
    f = open(file4, "r")
    file4_word = f.read().split()
    file4_word = list(map(lambda x: x.lower(), file4_word))
    dictionary = {}
    for i in file1_word:
        dictionary[i] = {file1.split('.txt')[0], }
    for i in file2_word:
        if i in file1_word:
            dictionary[i] = {file1.split('.txt')[0], file2.split('.txt')[0], }
        else:
            dictionary[i] = {file2.split('.txt')[0], }
    for i in file3_word:
        if i in file1_word and i in file2_word:
            dictionary[i] = {file1.split('.txt')[0], file2.split('.txt')[0], file3.split('.txt')[0], }
        elif i in file1_word:
            dictionary[i] = {file1.split('.txt')[0], file3.split('.txt')[0], }
        elif i in file2_word:
            dictionary[i] = {file1.split('.txt')[0], file2.split('.txt')[0], }
        else:
            dictionary[i] = {file3.split('.txt')[0], }
    for i in file4_word:
        if i in file1_word and i in file2_word and i in file3_word:
            dictionary[i] = {file1.split('.txt')[0], file2.split('.txt')[0], file3.split('.txt')[0],
                             file4.split('.txt')[0], }
        elif i in file1_word and i in file2_word:
            dictionary[i] = {file1.split('.txt')[0], file2.split('.txt')[0], file4.split('.txt')[0], }
        elif i in file1_word and i in file3_word:
            dictionary[i] = {file1.split('.txt')[0], file3.split('.txt')[0], file4.split('.txt')[0], }
        elif i in file2_word and i in file3_word:
            dictionary[i] = {file2.split('.txt')[0], file3.split('.txt')[0], file4.split('.txt')[0], }
        elif i in file1_word:
            dictionary[i] = {file1.split('.txt')[0], file4.split('.txt')[0], }
        elif i in file2_word:
            dictionary[i] = {file2.split('.txt')[0], file4.split('.txt')[0], }
        elif i in file3_word:
            dictionary[i] = {file3.split('.txt')[0], file4.split('.txt')[0], }
        else:
            dictionary[i] = {file4.split('.txt')[0], }
    return dictionary


def program_one1(file1, file2, file3, file4):
    def process_file(filename):
        f = open(filename, "r")
        words = f.read().split()
        words = list(map(lambda x: x.lower(), words))
        return set(words)

    dictionary = {}
    for filename in [file1, file2, file3, file4]:
        file_words = process_file(filename)
        file_name = filename.split('.txt')[0]
        for word in file_words:
            if word in dictionary:
                dictionary[word] |= {file_name}
            else:
                dictionary[word] = {file_name}
    return dictionary


def program_one3(file1, file2, file3, file4):
    def process_file(filename):
        f = open(filename, "r")
        words = f.read().split()
        words = list(map(lambda x: x.lower(), words))
        return set(words)

    def update_dictionary(dictionary, file_name, file_words):
        def update_word(d, word):
            if word in d:
                d[word] |= {file_name}
            else:
                d[word] = {file_name}
            return d
        return reduce(update_word, file_words, dictionary)
    file_names = [file1, file2, file3, file4]
    file_words = map(process_file, file_names)
    file_names = map(lambda x: x.split('.txt')[0], file_names)
    dictionary = reduce(lambda d, t: update_dictionary(d, t[0], t[1]), zip(file_names, file_words), {})
    d = open('dictionary.txt', 'w')
    d.write(str(dictionary))
    print(type(d))
    d.close()
    return repr('dictionary.txt')


print(program_one3('fruit.txt', 'colors.txt', 'cities.txt', 'names.txt'))
# l = list(map(lambda line:  line.strip(), f))
