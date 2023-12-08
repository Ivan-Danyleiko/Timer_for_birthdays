from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    today = date.today()
    next_week = today + timedelta(weeks=1)
    birthday_days = {}

    for user in users:
        name = user['name']
        birthday = user['birthday']
        birthday_date = datetime(
            today.year, birthday.month, birthday.day
        ).date()

        if birthday_date < today:
            next_year = today.year + 1
            birthday_date = datetime(
                next_year, birthday.month, birthday.day
            ).date()

        if today <= birthday_date < next_week:
            if birthday_date.weekday() in [5, 6]:
                birthday_date = (
                    today + timedelta(weeks=1, days=(0 - today.weekday()))
                )

            weekday = birthday_date.strftime('%A')
            birthday_days.setdefault(weekday, []).append(name)

    return birthday_days


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)

    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
