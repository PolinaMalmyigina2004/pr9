a = input("Введите число a: ")
b = input("Введите число b: ")

try:
  a = float(a)
  b = float(b)
except ValueError:
  print("Ошибка: Введите вещественные числа без символов.")
else:
  min_value = min(a, b)
  max_value = max(a, b)

  squares = [i**2 for i in range(int(min_value), int(max_value) + 1)]

  print("Список квадратов целых чисел между", a, "и", b, ":", squares)