from datetime import datetime, timedelta
from collections import defaultdict
from pprint import pprint


def make_list():
    users = []
    with open("list_collegs.txt") as fd:
        line = fd.readlines()
    for el in line:
        line_lst = el.strip("\n").split(" ")
        dict = {"name": line_lst[0], "birthday": datetime.strptime(
            line_lst[1], "%d-%m-%Y")}
        users.append(dict)
    return users


def get_next_week_start(d: datetime):
    diff_days = 7 - d.weekday()
    return d + timedelta(days=diff_days)


def prepare_birthday(d: datetime):
    try:
        return d.replace(year=datetime.now().year).date()
    except ValueError as e:
        return d.replace(year=datetime.now().year, day=28).date()


def get_birthdays_per_week(users):
    birthdays = defaultdict(list)

    today = datetime.now().date()

    next_week_start = get_next_week_start(today)
    start_period = next_week_start - timedelta(2)
    end_period = next_week_start + timedelta(4)

    happy_users = [user for user in users if start_period <=
                   prepare_birthday(user["birthday"]) <= end_period]
    for user in happy_users:
        current_bd = prepare_birthday(user["birthday"])
        if current_bd.weekday() in (5, 6):
            birthdays["Monday"].append(user["name"])
        else:
            birthdays[current_bd.strftime("%A")].append(user["name"])
    return birthdays


if __name__ == "__main__":
    users = make_list()
    result = get_birthdays_per_week(users)
    pprint(result)
