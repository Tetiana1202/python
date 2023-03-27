import random

# Запитати в користувача список страв
foods = input("Введіть список страв, розділених комами: ").split(",")

# Створити порожній масив для зберігання цін на страви
prices = {}

# Заповнити масив цінами на страви
for food in foods:
    prices[food.strip()] = round(random.uniform(5, 20), 2)

# Вивести чек із назвами страв та цінами
print("Кафе у Тетяни")
print("===")

# Порахувати загальну суму
sum = 0
for food, price in prices.items():
    print(food + ": " + str(price) + " грн")
    sum += price

print("Всього: " + str(sum) + " грн")
print("===")
