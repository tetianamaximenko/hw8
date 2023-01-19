from datetime import datetime, timedelta

users = [
    {'name_user': 'Ann', 'birthday': datetime(1979, 10, 22)},
    {'name_user': 'Pavlo', 'birthday': datetime(1984, 2, 2)},
    {'name_user': 'Tina', 'birthday': datetime(2009, 3, 23)},
    {'name_user': 'Fill', 'birthday': datetime(2007, 12, 17)},
    {'name_user': 'Kim', 'birthday': datetime(2007, 12, 15)},
    {"name_user": "Tanya", "birthday": datetime(year=1992, month=9, day=23)},
    {"name_user": "Kostya", "birthday": datetime(year=1992, month=3, day=8)},
    {"name_user": "Serhiy", "birthday": datetime(year=1992, month=3, day=8)},
    {"name_user": "Jane", "birthday": datetime(year=1994, month=11, day=3)},
    {"name_user": "Nastya", "birthday": datetime(year=1989, month=12, day=24)},
    {"name_user": "Vasya", "birthday": datetime(year=1986, month=12, day=24)},
    {"name_user": "Polina", "birthday": datetime(year=1986, month=12, day=21)},
    {"name_user": "Lilia", "birthday": datetime(year=1995, month=12, day=21)}
]

# def get_birthdays_per_week(users):


def main(users, n=7):
    present_day = datetime.now()
    for count_n in range(n+1):
        period_date_birth = present_day + timedelta(days=count_n)
        join_user = ''
        for user in users:
            current_year = user['birthday'].replace(year=present_day.year)
            if current_year.date() == period_date_birth.date():
                current_year_weekday = current_year.weekday()
                if current_year_weekday == 5:
                    current_year = period_date_birth + timedelta(days=2)
                if current_year_weekday == 6:
                    current_year = period_date_birth + timedelta(days=1)
                if join_user == '':
                    a = current_year.strftime('%A')
                    join_user = join_user + a + ': ' + user['name_user']
                else:
                    join_user = join_user + ', ' + user['name_user']
        if join_user != '':
            print(join_user)


# -------------------------------------------------------------------------------------


if __name__ == '__main__':

    main(users)
