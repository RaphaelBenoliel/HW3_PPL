from functools import reduce


def program_one(input_file1, input_file2, input_file3, input_file4):
    """
        Reads the given input files, creates a dictionary mapping words to sets of file names, and writes the
        dictionary to a file.
        :param input_file1: A string representing the file path of the first input file.
        :param input_file2: A string representing the file path of the second input file.
        :param input_file3: A string representing the file path of the third input file.
        :param input_file4: A string representing the file path of the fourth input file.
        :return: A string representing the file path of the dictionary file.
        """
    def process_file(file_name):
        """
        Reads the given file, splits its contents into a list of words, and returns the set of lowercase words.
        :param file_name: A string representing the file path.
        :return: A set of strings.
        """
        f = open(file_name, "r")
        words = f.read().split()
        words = list(map(lambda word: word.lower(), words))
        return set(words)

    def update_dictionary(dict_arg, file_name, file_w):
        """
        Updates the given dictionary by adding the given file name and its set of words to the dictionary.
        :param dict_arg: A dictionary mapping words to sets of file names.
        :param file_name: A string representing the file name.
        :param file_w: A set of strings.
        :return: The updated dictionary.
        """
        def update_word(dic, word):
            """
            Updates the given dictionary by adding the given word and file name to the dictionary.
            :param dic: A dictionary mapping words to sets of file names.
            :param word: A string representing the word to add to the dictionary.
            :return: The updated dictionary.
            """
            if word in dic:
                dic[word] |= {file_name}
            else:
                dic[word] = {file_name}
            return dic
        return reduce(update_word, file_w, dict_arg)

    file_names = [input_file1, input_file2, input_file3, input_file4]
    file_words = map(process_file, file_names)
    file_names = map(lambda fname: fname.split('.txt')[0], file_names)
    dictionary = reduce(lambda dic, file: update_dictionary(dic, file[0], file[1]), zip(file_names, file_words), {})
    dict_file = open('dictionary.txt', 'w')
    dict_file.write(str(dictionary))
    dict_file.close()
    return repr('dictionary.txt')


print(program_one('fruit.txt', 'colors.txt', 'cities.txt', 'names.txt'))
