price_per_console = float(input("Введіть вартість однієї ігрової приставки: "))
quantity = int(input("Введіть кількість ігрових приставок: "))
discount_percentage = float(input("Введіть відсоток знижки (якщо немає, введіть 0): "))
choice = input("Оберіть, що потрібно порахувати (загальну суму - 'с', вартість однієї - 'в'): ")

if choice == 'с':
    total_price = price_per_console * quantity * (1 - discount_percentage / 100)
    print(f"Загальна сума замовлення зі знижкою дорівнює {total_price:.2f} грн.")
elif choice == 'в':
    price_with_discount = price_per_console * (1 - discount_percentage / 100)
    print(f"Вартість однієї приставки зі знижкою дорівнює {price_with_discount:.2f} грн.")
else:
    print("Ви ввели некоректний вибір.")
