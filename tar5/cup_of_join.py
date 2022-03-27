def join(*lists, sep='-'):
      """
    :param lists:
    :param sep: to be between the lists
    :return: A new list from a combination of all the lists we received with a mark between them
    """
    if len(lists) == 0:
        return None
    new_list = []
    for list in lists:
        new_list+=list
        new_list.append(sep)
    return new_list[:-1]


def main():
    print(join(sep='/'))
    print(join([1, 2], [8], [9, 5, 6], sep='@'))
    print(join([1, 2], [8], [9, 5, 6]))
    print(join([1]))


if __name__ == "__main__":
    main()
