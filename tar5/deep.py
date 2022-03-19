import glob


def deep():
    path = input("enter path:")
    my_files = glob.glob(path + "\deep*")
    for file in my_files:
        print(file[len(path) + 1:])


deep()
