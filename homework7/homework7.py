def cyclic_shift_right(numbers):
    """
    Функция циклически сдвигает элементы списка вправо на 1 позицию.
    """

    if len(numbers) <= 1:
        print("Список пустой или содержит один элемент. Нечего сдвигать.")
        return numbers

    # Проверка на корректность данных
    for num in numbers:
        if not isinstance(num, int) and not isinstance(num, float):
            print("Ошибка: В списке найдены не числовые данные.")
            return numbers

    last_element = numbers[-1]  # Сохраняем последний элемент
    for i in range(len(numbers) - 1, 0, -1):  # Сдвигаем элементы вправо
        numbers[i] = numbers[i - 1]
    numbers[0] = last_element  # Устанавливаем последний элемент на первую позицию

    print("Измененный список:", numbers)


# Ввод данных от пользователя
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

# Вызов функции сдвига
cyclic_shift_right(numbers)




