
def make_rlist(first, rest):
    return (first, rest)


def first(s):
    return s[0]


def rest(s):
    return s[1]


def len_rlist(s):
    length = 0
    while s != empty_rlist:
        s, length = rest(s), length + 1
    return length


def getitem_rlist(lst, index):
    while index > 0:
        lst, index = rest(lst), index - 1
    return first(lst)


def make_mutable_rlist(other=None):
    contents = empty_rlist
    if other != None:
        index = other['length']() - 1
        while index >= 0:
            contents = make_rlist(other['get_item'](index), contents)
            index -= 1

    def length():
        return len_rlist(contents)

    def get_item(ind):
        return getitem_rlist(contents, ind)

    def push_first(value):
        nonlocal contents
        contents = make_rlist(value, contents)

    def pop_first():
        nonlocal contents
        f = first(contents)
        contents = rest(contents)
        return f

    def slice(indexf, indexl):
        new = make_mutable_rlist()
        temp = make_mutable_rlist()
        t = contents
        while indexf > 0:
            indexf -= 1
            indexl -= 1
            t = rest(t)
        while (indexl > 0):
            new['push_first'](first(t))
            t = rest(t)
            indexl -= 1
        while new['length']() > 0:
            temp['push_first'](new['pop_first']())
        return temp

    def extend(other_list):
        size_other = other_list['length']()
        size_this = length()
        new_list = empty_rlist
        for i in range(size_other - 1, -1, -1):
            new_list = make_rlist(other_list['get_item'](i), new_list)
        for i in range(size_this - 1, -1, -1):
            new_list = make_rlist(get_item(i), new_list)
        nonlocal contents
        contents = new_list

    def str():
        string = '['
        t = contents
        while t is not empty_rlist:
            temp = first(t)
            t = rest(t)
            string += '{0}'.format(temp)
            if t != None:
                string += ','
        string += ']'
        print(string)

    def get_iterator():
        index = 0

        def hasNext():
            if index == length():
                return False
            return True

        def next():
            nonlocal index
            index += 1
            if index - 1 < length():
                return get_item(index - 1)

        return {'hasNext': hasNext, 'next': next}

    return {'length': length, 'get_item': get_item, 'push_first': push_first, 'pop_first': pop_first, 'str': str, 'slice':slice, 'extend':extend, 'get_iterator':get_iterator}


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