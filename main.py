# Запит на введення розміру файлу в гігабайтах
file_size_gb = float(input("Введіть розмір файлу в гігабайтах: "))

# Запит на введення швидкості інтернет-з'єднання в бітах на секунду
internet_speed_bps = float(input("Введіть швидкість інтернет-з'єднання в бітах на секунду: "))

# Запит на вибір одиниці часу
time_unit = input("Виберіть одиницю часу (години, хвилини, секунди): ")

# Конвертуємо розмір файлу в біти
file_size_bps = file_size_gb * 8 * 1e9

# Розраховуємо час завантаження файла
if time_unit == "години":
    time = file_size_bps / (internet_speed_bps * 3600)
elif time_unit == "хвилини":
    time = file_size_bps / (internet_speed_bps * 60)
elif time_unit == "секунди":
    time = file_size_bps / internet_speed_bps
else:
    print("Непідтримувана одиниця часу")
    time = None

if time is not None:
    print(f"Час завантаження файла: {time:.2f} {time_unit}")
