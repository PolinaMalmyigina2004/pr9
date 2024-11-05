numbers = [] 

even_count = 0 
odd_count = 0 

while True:
  user_input = input("Введите число (или 'end' для завершения): ")
  if user_input == "end":
    break

  try:
    number = float(user_input)
    numbers.append(number) 
    if number % 2 == 0:
      even_count += 1
    else:
      odd_count += 1
  except ValueError:
    print("Ошибка: Введите число или 'end'.")

print("Введенные числа:", numbers)
print("Количество четных чисел:", even_count)
print("Количество нечетных чисел:", odd_count)
