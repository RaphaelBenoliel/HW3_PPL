def third_program():
    # Read the list of tuples from the words.txt file
    with open('words.txt', 'r') as f:
        tuples = eval(f.read())

    def filter_func(tup):
        """
        Filters tuples based on the number of occurrences and number of categories.
        :param tup: A tuple containing a word, the number of occurrences of that word, and a set of categories to
        which the word belongs.
        :return: True if the tuple meets the filtering criteria, False otherwise.
        """
        word, occurrences, categories = tup
        return occurrences >= 5 or len(categories) > 1

    def generate_message(tup):
        """
        Generates a message for the given tuple.
        :param tup: A tuple containing a word, the number of occurrences of that word, and a set of categories to
        which the word belongs.
        :return: A string representing the message.
        """
        word, occurrences, categories = tup
        condition1 = occurrences >= 5 and len(categories) > 1
        condition2 = occurrences >= 5
        condition3 = len(categories) > 1
        condition_tup = (condition1, condition2, condition3)
        dic_res = {(True, True, True): f"'{word}' because it belongs to at least two categories and because it"
                                 f" appears at least five times", (False, True, False): f"'{word}' because it "
                                 f"appears at least five times", (False, False, True): f"'{word}' because it belongs "
                                 f"to at least two categories"}
        return dic_res[condition_tup]
    filtered_tuples = filter(filter_func, tuples)
    messages = map(generate_message, filtered_tuples)
    result = '\n'.join(messages)
    print(result)


# Running the program:
third_program()

