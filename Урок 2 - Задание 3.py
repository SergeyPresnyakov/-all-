"""Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
 (зима, весна, лето, осень). Напишите решения через list и через dict. """

# Решение со списками

seasons = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
name_seasons = ["Зима", "Весна", "Лето", "Осень"]

print("Решение со списками")
while True:
    num_month = int(input("Введите номер месяца (целое число от 1 до 12): "))
    if num_month > 12 or num_month < 1:
        print("Вы ввели неправильный номер")
        continue
    else:
        break

for num_season in range(4):
    if num_month in seasons[num_season]:
        print("Номер месяца, который Вы ввели, относится к времени года:", name_seasons[num_season])

print("")
print("Решение со словарем")

# Решение со словарем и списком

seasons = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}

while True:
    num_month = int(input("Введите номер месяца (целое исло от 1 до 12): "))
    if num_month > 12 or num_month < 1:
        print("Вы ввели неправильный номер")
        continue
    else:
        break

for season in seasons.keys():
    if num_month in seasons.get(season):
        print("Номер месяца, который Вы ввели, относится к времени года:", season)
