def join(*lists, sep='-'):
    if len(lists) == 0:
        return None
    new_list = []
    for list in lists:
        new_list+=list
        new_list.append(sep)
    return new_list[:-1]


print(join(sep='/'))
print(join([1, 2], [8], [9, 5, 6], sep='@'))
print(join([1, 2], [8], [9, 5, 6]))
print(join([1]))

