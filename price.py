# price = 100
# discount = 5

# price_with_discount = price - price * discount / 100

# print(price_with_discount)



def get_summ(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    result = one + delimiter + two
    return result.upper()


string_result = get_summ("Learn", "python")
print(string_result)


def format_price(price):
    return f"Цена: {int(price)} руб."


result = format_price(56.24)
print(result)