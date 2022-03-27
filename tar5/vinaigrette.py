from random import randrange
from datetime import timedelta
from datetime import datetime
import calendar


def random_date(start_date, end_date):
    """
    This function get two datetime objects: start and end.
    return a random datetime between two datetime objects.
    """
    delta = end_date - start_date
    int_delta = (delta.days * 24 * 60 * 60)
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


def if_monday():
    """
    The function picks up two dates from the user and sends to the function for a random date between them.
    For a date that is Monday a message will be printed
    """
    start_date = datetime.strptime(input("Enter Date 1: "), '%m-%d-%Y')
    end_date = datetime.strptime(input("Enter Date 2: "), '%m-%d-%Y')
    my_date = random_date(start_date, end_date)
    print(my_date)
    if calendar.day_name[my_date.weekday()] == 'Monday':
        print("I do not have vinaigrette!")


def main():
    if_monday()


if __name__ == "__main__":
    main()
