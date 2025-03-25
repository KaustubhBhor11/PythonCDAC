import datetime as dt

today = dt.datetime.now()
d = dt.datetime(2022, 1, 23)
print(d.strftime("%x"))
print(d)
print(today)


def calculate_age(string):  # expects date in format yyyy/mm/dd
    today_date = dt.datetime.now()
    b_day_list = string.split("/")
    b_day_list = dt.datetime(int(b_day_list[0]), int(b_day_list[1]), int(b_day_list[2]))
    age = today_date - b_day_list
    print(age)
    return int(age.days / 365)


print(calculate_age("1996/03/28"))
