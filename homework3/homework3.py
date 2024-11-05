numbers = [] 

while True:
  user_input = input("Введите число (или 'end' для завершения): ")
  if user_input == "end":
    break

  try:
    number = float(user_input)
    numbers.append(number) 
  except ValueError:
    print("Ошибка: Введите число или 'end'.")

print("Нечетные элементы списка:", end=" ")
for number in numbers:
  if number % 2 != 0:
    print(number, end=" ")