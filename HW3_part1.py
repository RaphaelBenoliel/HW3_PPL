

def year(obj):
    """
    Prints the year of the given date object.
    :param obj: A date object.
    """
    print(obj('year')())


def month(obj):
    """
    Prints the month of the given date object.
    :param obj: A date object.
    """
    print(obj('month')())


def day(obj):
    """
    Prints the day of the given date object.
    :param obj: A date object.
    """
    print(obj('day')())


def str_date(obj):
    """
    Prints the date in the format "day[st, nd, rd, th] of month, year".
    :param obj: A date object.
    """
    if obj('day')() in (1, 21, 31):
        print(f"{obj('day')()}st of {obj('month')()}, {obj('year')()}")
    elif obj('day')() in (2, 22):
        print(f"{obj('day')()}nd of {obj('month')()}, {obj('year')()}")
    elif obj('day')() in (3, 23):
        print(f"{obj('day')()}rd of {obj('month')()}, {obj('year')()}")
    else:
        print(f"{obj('day')()}th of {obj('month')()}, {obj('year')()}")


def make_date(year, month, day):
    """
    Creates a date object.
    :param year: An integer representing the year (e.g. 2021).
    :param month: An integer representing the month (1-12).
    :param day: An integer representing the day of the month (1-31).
    :return: A date object.
    """
    def get_year():
        """
        Returns the year of the date object.
        :return: An integer representing the year.
        """
        return year

    def get_month():
        """
        Returns the month of the date object as a string.
        :return: A string representing the month (e.g. "January").
        """
        if month == 1:
            return "January"
        elif month == 2:
            return "February"
        elif month == 3:
            return "March"
        elif month == 4:
            return "April"
        elif month == 5:
            return "May"
        elif month == 6:
            return "June"
        elif month == 7:
            return "July"
        elif month == 8:
            return "August"
        elif month == 9:
            return "September"
        elif month == 10:
            return "October"
        elif month == 11:
            return "November"
        elif month == 12:
            return "December"

    def get_day():
        """
        Returns the day of the month of the date object.
        :return: An integer representing the day of the month.
        """
        return day

    def dispatch(msg):
        """
        Dispatches the message to the appropriate internal function.
        :param msg: A string indicating which function to return.
        :return: A function.
        """
        if msg == 'year':
            return get_year
        if msg == 'month':
            return get_month
        if msg == 'day':
            return get_day
    return dispatch


d = make_date(2022, 12, 31)
print(d)
year(d)
month(d)
day(d)
str_date(d)
