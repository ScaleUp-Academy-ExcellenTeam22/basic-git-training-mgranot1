from random import randrange
from datetime import timedelta
from datetime import datetime
import calendar


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60)
    random_second = randrange(int_delta)
    return start + timedelta()


def if_monday():
    d1 = datetime.strptime(input("enter date 1: "), '%m-%d-%Y')
    d2 = datetime.strptime(input("enter date 2: "), '%m-%d-%Y')
    my_date = random_date(d1, d2)
    print(my_date)
    if calendar.day_name[my_date.weekday()] == 'Monday':
        print("I do not have vinaigrette!")


if_monday()
