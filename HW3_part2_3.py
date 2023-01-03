
# Read the list of tuples from the words.txt file
with open('words.txt', 'r') as f:
    tuples = eval(f.read())


# Define a function that generates the message for a given tuple
def generate_message(t):
    """
    Generates a message for a given tuple.
    Parameters: t (tuple): A tuple consisting of a word, the number of times it appears in the text, and the categories
     it belongs to.
    Returns: str: A message indicating why the word passed the filter.
    """
    word, occurrences, categories = t
    if occurrences >= 5 and len(categories) > 1:
        return f"'{word}' because it belongs to at least two categories and because it appears at least five times"
    elif occurrences >= 5:
        return f"'{word}' because it appears at least five times"
    elif len(categories) > 1:
        return f"'{word}' because it belongs to at least two categories"


# Define the filter function
def filter_func(t):
    """
    Filters a tuple based on the conditions specified in the task.

    Parameters:
    t (tuple): A tuple consisting of a word, the number of times it appears in the text, and the categories it belongs to.

    Returns:
    bool: `True` if the tuple passes the filter, `False` otherwise.
    """
    word, occurrences, categories = t
    return occurrences >= 5 or len(categories) > 1

"""
Filters the tuples in the words.txt file and prints a message for each word that passes the filter.
"""
# Filter the tuples using the filter function
filtered_tuples = filter(filter_func, tuples)

# Generate the messages for the filtered tuples using the generate_message function
messages = map(generate_message, filtered_tuples)

# Join the messages into a single string
result = '\n'.join(messages)

print(result)
