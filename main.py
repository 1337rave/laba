import math
diameter = float(input("Введіть діаметр кола: "))
choice = input("Оберіть, що потрібно порахувати (площу - 'п', периметр - 'пр'): ")
if choice == 'п':
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    print(f"Площа кола з діаметром {diameter} дорівнює {area:.2f}.")
elif choice == 'пр':
    circumference = math.pi * diameter
    print(f"Периметр кола з діаметром {diameter} дорівнює {circumference:.2f}.")
else:
    print("Ви ввели некоректний вибір.")
