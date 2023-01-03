from functools import reduce


def program_one(file1, file2, file3, file4):
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
    d.close()
    return repr('dictionary.txt')


print(program_one('fruit.txt', 'colors.txt', 'cities.txt', 'names.txt'))
# l = list(map(lambda line:  line.strip(), f))
