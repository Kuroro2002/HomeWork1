# from datetime import datetime
#
#
# def get_days():
#     user_input = input("Введіть вашу дату у форматі РРРР-ММ-ДД:")
#     user_data = datetime.strptime(user_input, '%Y-%m-%d')
#     today_date = datetime.today()
#     user_data = user_data.replace(year=today_date.year)
#     resalt = user_data - today_date
#     print( resalt.days)
#
#
# if __name__ == "__main__":
#     get_days()
 #Task 2
# import random
#
# def get_numbers_ticket(min_value, max_value, quantity):
#
#
#     if min_value >= 1 or min_value <= 999 and max_value <= 1000 and quantity in range(min_value, max_value + 1):
#         numbers = list(range(min_value, max_value + 1))
#         random.shuffle(numbers)
#         return numbers[:quantity]
#     else:
#         raise ValueError("Некоректні параметри")
#
#
# min_value = int(input("Введіть мінімальне значення (1-999): "))
# max_value = int(input("Введіть максимальне значення (1-1000): "))
# quantity = int(input("Введіть кількість чисел: "))
#
#
# try:
#     generated_numbers = get_numbers_ticket(min_value, max_value, quantity)
#     print("Згенеровані числа:", sorted(generated_numbers))
# except ValueError as e:
#     print("Помилка:", e)


# Task 3
# import re
#
# raw_numbers = [
#     "067\\t123 4567",
#     "(095) 234-5678\\n",
#     "+380 44 123 4567",
#     "380501234567",
#     "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   ",
# ]
#
# def normalize_phone(phone_number):
#     pattern = r"[\d\+]+"
#     phone_number=re.findall(pattern,phone_number)
#     phone_number="".join(phone_number)
#
#     if len(phone_number)==12:
#         phone_number="+"+phone_number
#     elif len(phone_number)==10:
#         phone_number="+38"+phone_number
#     return phone_number
#
#
# sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
# print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
#
#
#Task 4
# from datetime import datetime, timedelta
#
# def get_upcoming_birthdays(users):
#     today = datetime.today().date()
#     upcoming_birthdays = []
#
#     for user in users:
#         birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
#
#
#         if birthday_date < today:
#
#             birthday_date = birthday_date.replace(year=today.year + 1)
#
#
#         days_until_birthday = (birthday_date - today).days
#
#         if 0 <= days_until_birthday <= 6:
#             if birthday_date.weekday() in [5, 6]:
#                 days_until_birthday += (7 - birthday_date.weekday())
#
#             congratulation_date = today + timedelta(days=days_until_birthday)
#             user_info = {"name": user["name"], "congratulation_date": congratulation_date.strftime("%Y.%m.%d")}
#             upcoming_birthdays.append(user_info)
#
#     return upcoming_birthdays
#
# users = [
#     {"name": "John Doe", "birthday": "1985.02.10"},
#     {"name": "Jane Smith", "birthday": "1990.01.27"},
#     {"name": "Mike Jones", "birthday": "2000.02.05"},
# ]
#
# upcoming_birthdays = get_upcoming_birthdays(users)
# print("Список привітань на цьому тижні:", upcoming_birthdays)

