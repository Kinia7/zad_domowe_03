from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    today = datetime.now().date()
  
    birthdays_this_week = []

    for user in users:
        days_until_birthday = (user['birthday'].date() - today).days
        if days_until_birthday <= 7 and days_until_birthday >= 0:
            birthdays_this_week.append(user)

    # Przesuń życzenia dla użytkowników, których urodziny wypadły w weekend, na poniedziałek
    for user in birthdays_this_week:
        if user['birthday'].weekday() >= 5:  # Weekend (sobota lub niedziela)
            user['birthday'] += timedelta(days=(7 - user['birthday'].weekday()))

    if birthdays_this_week:
        print("Użytkownicy, którym należy złożyć życzenia z okazji urodzin w tym tygodniu:")
        for user in birthdays_this_week:
            day_of_week = user['birthday'].strftime('%A')
            print(f"{user['name']}: {day_of_week}")
    else:
        print("Brak urodzin do świętowania w tym tygodniu.")

# Przykładowa lista użytkowników (testowa)
users_list = [
    {'name': 'Anna', 'birthday': datetime(2024, 1, 28)},
    {'name': 'Jan', 'birthday': datetime(2024, 1, 30)},
    {'name': 'Katarzyna', 'birthday': datetime(2024, 2, 5)},
]

get_birthdays_per_week(users_list)
