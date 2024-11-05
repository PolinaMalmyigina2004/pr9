import random

numbers = [random.randint(-10, 10) for _ in range(10)]

print("Исходный список:", numbers)

# Проверка на корректность данных в списке
for num in numbers:
  if not isinstance(num, int) and not isinstance(num, float):
    print("Ошибка: В списке найдены не числовые данные.")
    break

# Выводим элементы, большие предыдущего
print("Элементы, большие предыдущего:", end=" ")
for i in range(len(numbers)):
  if i == 0: # Для первого элемента сравниваем с последним
    if numbers[i] > numbers[-1]:
      print(numbers[i], end=" ")
  else:
    if numbers[i] > numbers[i - 1]:
      print(numbers[i], end=" ")