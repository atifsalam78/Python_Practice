from datetime import datetime as d
from datetime import timedelta
from random import randrange


def random_date(start, end):
    delta = end - start
    # print(delta)
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    # print(int_delta)
    random_second = randrange(int_delta)
    # print(random_second)
    return start + timedelta(seconds=random_second)


date1 = d.strptime('1970-01-01-01-30', '%Y-%m-%d-%H-%M')
date2 = d.strptime('2023-01-01-04-50', '%Y-%m-%d-%H-%M')
rand_date = random_date(date1, date2)

print(rand_date.strftime('%Y-%m-%d-%H-%M'))