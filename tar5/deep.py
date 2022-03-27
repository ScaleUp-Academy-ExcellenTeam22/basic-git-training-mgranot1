import glob



def deep():
    """
    print list of files called deep...
    """
    path = input("Enter Path: ")
    my_files = glob.glob(path + r"\deep*")
    print([file[len(path) + 1:] for file in my_files])


def main():
    deep()


if __name__ == "__main__":
    main()

