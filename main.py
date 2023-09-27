# Запит на введення кількості годин
hours = int(input("Введіть кількість годин: "))

# Перевірка, до якого діапазону входить введене число
if 0 <= hours < 6:
    print("Good Night")
elif 6 <= hours < 13:
    print("Good Morning")
elif 13 <= hours < 17:
    print("Good Day")
elif 17 <= hours <= 23:
    print("Good Evening")
else:
    print("Некоректне введення годин")
