

def make_currency(amount, symbol):
    """
    Creates a currency object with the given amount and symbol.
    :param amount: The amount of currency represented by the object.
    :param symbol: The symbol representing the currency (e.g. '$', '€').
    :return: A function that can be used to retrieve or modify the amount or symbol, or to convert the currency
    to a new symbol.
    """
    def get_value(msg):
        """
        Retrieves the value of the given attribute.
        :param msg: A string representing the name of the attribute to retrieve.
        :return: The value of the attribute.
        """
        if msg == 'amount':
            return amount
        else:
            return symbol

    def set_value(msg, value):
        """
        Sets the value of the given attribute.
        :param msg: A string representing the name of the attribute to set.
        :param value: The new value for the attribute.
        """
        nonlocal amount, symbol
        if msg == 'amount':
            amount = value
        elif msg == 'symbol':
            symbol = value
        else:
            print(f'No such attribute {msg}')

    def convert(conversion_func, new_symbol):
        """
        Converts the currency to a new symbol using the given conversion function.
        :param conversion_func: A function that takes an amount and returns the converted amount.
        :param new_symbol: A string representing the new symbol for the currency.
        """
        nonlocal amount, symbol
        amount = conversion_func(amount)
        symbol = new_symbol

    def str_value():
        """
        Returns a string representation of the currency object.
        :return: A string in the format "symbolamount" (e.g. "$100.00")
        """
        return f"{symbol}{amount:.2f}"

    def dispatch(message):
        """
        Dispatches the given message to the appropriate function.
        :param message: A string representing the message to dispatch.
        :return: The result of the dispatched function.
        """
        if message == 'get_value':
            return get_value
        elif message == 'set_value':
            return set_value
        elif message == 'convert':
            return convert
        elif message == 'str':
            return str_value
    return dispatch


# Running examples:
c = make_currency(10.50, '$')
print(c('get_value')('amount'))
print(c('get_value')('symbol'))
c('set_value')('amount', 50)
print(c('get_value')('amount'))
print(c('str')())
c('convert')(lambda x: x * 3.87, '₪')
print(c('str')())
