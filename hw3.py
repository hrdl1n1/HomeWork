# Перше завдання

from datetime import datetime

def get_days_from_today(date):
    try:
        # Перетворюємо дату у форматі 'РРРР-ММ-ДД' у datetime
        input_date = datetime.strptime(date, '%Y-%m-%d')
        
        # поточна дата
        current_date = datetime.today()
        
        # Різницю між поточною датою та заданою датою у днях
        days_difference = (current_date - input_date).days
        
        return days_difference
    except ValueError:
        # Обробка винятку у разі неправильного формату вхідних даних
        return "Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'."

# Приклад використання коду 
date_string = '2020-10-09'
result = get_days_from_today(date_string)

print(f"Кількість днів між {date_string} і поточною датою: {result}")


# Друге завдання

import random

def get_numbers_ticket(min, max, quantity):
    # Перевірка коректності вхідних параметрів
    if not (1 <= min <= max <= 1000) or not (1 <= quantity <= max - min + 1):
        return []

    # Використання множини для унікальності чисел
    unique_numbers = set()

    while len(unique_numbers) < quantity:
        # Додавання випадкового числа
        unique_numbers.add(random.randint(min, max))

    # Повернення відсортованого списку
    return sorted(list(unique_numbers))

# Приклад використання коду
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)


# Третє завдання

import re

def normalize_phone(phone_number):
    # Видалення всіх символів, крім цифр та '+'
    cleaned_number = re.sub(r'[^0-9+]', '', phone_number)

    # чи номер починається з '+' ?
    if not cleaned_number.startswith('+'):
        # Додаємо +38
        cleaned_number = '+38' + cleaned_number.lstrip('38')

    return cleaned_number

# Приклад використання коду
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

good_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", good_numbers)


# Четверте завдання

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