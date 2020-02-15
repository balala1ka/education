def get_summ(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    result = str(one + str(delimiter) + two)
    return result


print(get_summ('Learn', 'Python'))
