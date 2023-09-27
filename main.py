input_seconds = int(input("Введіть час у секундах, що минув від початку дня: "))
hours = input_seconds // 3600
minutes = (input_seconds % 3600) // 60
seconds = input_seconds % 60
print(f"До опівночі залишилося {hours} годин, {minutes} хвилин і {seconds} секунд.")
