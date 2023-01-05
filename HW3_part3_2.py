

def make_rlist(r_first, r_rest):
    """
    Constructs a new immutable rlist with the given first element and rest.
    :param r_first: The first element of the rlist.
    :param r_rest: The rest of the rlist.
    :return: A new rlist with the given first element and rest.
    """
    return r_first, r_rest


def first(rlist):
    """
    Returns the first element of the given rlist.
    :param rlist: The rlist to get the first element from.
    :return: The first element of the rlist.
    """
    return rlist[0]


def rest(rlist):
    """
    Returns the rest of the given rlist.
    :param rlist: The rlist to get the rest of.
    :return: The rest of the rlist.
    """
    return rlist[1]


def len_rlist(rlist):
    """
    Returns the length of the given rlist.
    :param rlist: The rlist to get the length of.
    :return: The length of the rlist.
    """
    length = 0
    while rlist != empty_rlist:
        rlist, length = rest(rlist), length + 1
    return length


def getitem_rlist(lst, index):
    """
    Returns the element at the given index in the given rlist.
    :param lst: The rlist to get the element from.
    :param index: The index of the element to get.
    :return: The element at the given index in the rlist.
    """
    while index > 0:
        lst, index = rest(lst), index - 1
    return first(lst)


def make_mutable_rlist(other=None):
    """
    Create a new mutable rlist with the optional parameter 'other' as its initial contents.
    :param other: The initial contents of the rlist (optional)
    :return: The new mutable rlist
    """
    contents = empty_rlist
    if other is not None:
        index = other['length']() - 1
        while index >= 0:
            contents = make_rlist(other['get_item'](index), contents)
            index -= 1

    def length():
        """
        Get the length of the rlist.
        :return: The length of the rlist.
        """
        return len_rlist(contents)

    def get_item(ind):
        """
            Get the item at the given index of the rlist.
            :param ind: The index of the item to get.
            :return: The item at the given index.
            """
        return getitem_rlist(contents, ind)

    def push_first(value):
        nonlocal contents
        contents = make_rlist(value, contents)

    def pop_first():
        nonlocal contents
        fst = first(contents)
        contents = rest(contents)
        return fst

    def rlist_slice(start, end):
        new = make_mutable_rlist()
        result = make_mutable_rlist()
        current = contents
        while start > 0:
            start -= 1
            end -= 1
            current = rest(current)
        while end > 0:
            new['push_first'](first(current))
            current = rest(current)
            end -= 1
        while new['length']() > 0:
            result['push_first'](new['pop_first']())
        return result

    def extend(other_list):
        other_size = other_list['length']()
        curr_size = length()
        new_list = empty_rlist
        for i in range(other_size - 1, -1, -1):
            new_list = make_rlist(other_list['get_item'](i), new_list)
        for i in range(curr_size - 1, -1, -1):
            new_list = make_rlist(get_item(i), new_list)
        nonlocal contents
        contents = new_list

    def rlist_str():
        string = '['
        current = contents
        while current is not empty_rlist:
            temp = first(current)
            current = rest(current)
            string += '{0}'.format(temp)
            if current is not None:
                string += ','
        string += ']'
        print(string)

    def get_iterator():
        i = 0

        def hasNext():
            if i == length():
                return False
            return True

        def Next():
            nonlocal i
            i += 1
            if i - 1 < length():
                return get_item(i - 1)
        return {'hasNext': hasNext, 'next': Next}
    return {'length': length, 'get_item': get_item, 'push_first': push_first, 'pop_first': pop_first, 'str': rlist_str,
            'slice': rlist_slice, 'extend': extend, 'get_iterator': get_iterator}


empty_rlist = None
my_list = make_mutable_rlist()
for x in range(4):
    my_list['push_first'](x)
my_list['str']()
my_list['slice'](0, 2)['str']()
ext = my_list
my_list['extend'](ext)
my_list['str']()
your_list = make_mutable_rlist(my_list)
your_list['str']()
it = my_list['get_iterator']()
while it['hasNext']():
    print(it['next']())