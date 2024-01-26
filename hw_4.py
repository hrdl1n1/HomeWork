from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_bdays = []

    for user in users:
        bday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # Скільки днів до next birthday
        days_until_bday = (datetime(today.year, bday.month, bday.day).date() - today).days

        # чи день народження випадає вперед на 7 днів - сьогодні включно
        if 0 <= days_until_bday <= 7:
            if bday.weekday() >= 5:  # 5 - Субота, 6 - Неділя
                days_until_monday = (7 - bday.weekday())
                bday += timedelta(days_until_monday)

            # Додавання інформації про користувача та дату привітання до списку
            upcoming_bdays.append({
                "name": user["name"],
                "congratulation_date": bday.strftime("%Y.%m.%d")
            })

    return upcoming_bdays

# Приклад використання коду
users = [
    {"name": 'John Doe', "birthday": '1985.01.23'},
    {"name": 'Jane Smith', "birthday": '1990.01.26'}, 
    {"name": 'Nick Darsel', "birthday": '1984.01.27'}, 
    {"name": 'Ethan Williams', "birthday": '1970.01.30'}, 
    {"name": 'Liam Smith', "birthday": '1995.01.20'}, 
    {"name": 'John Doe', "birthday": '1985.02.03'}, 
    {"name": 'Jane Smith', "birthday": '1990.01.28'}
]

upcoming_bdays = get_upcoming_birthdays(users)
print("Привітати на цьому тижні:", upcoming_bdays)