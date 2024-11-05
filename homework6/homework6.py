def swap_min_max(numbers):
    if not numbers:
        return "Список пуст. Нечего менять."
    
    if len(numbers) == 1:
        return "Список состоит из одного элемента. Ничего не меняем."

    filtered_numbers = []
    for num in numbers:
        try:
            filtered_numbers.append(float(num))
        except ValueError:
            print(f"Значение '{num}' не является числом.Введите число.")

    if not filtered_numbers:
        return "После фильтрации не осталось числовых значений."

    min_value = min(filtered_numbers)
    max_value = max(filtered_numbers)

    if min_value == max_value:
        return "Максимальный и минимальный элементы одинаковы, ничего не меняем."

    min_index = filtered_numbers.index(min_value)
    max_index = filtered_numbers.index(max_value)
    filtered_numbers[min_index], filtered_numbers[max_index] = filtered_numbers[max_index], filtered_numbers[min_index]

    return filtered_numbers

def main():
    user_input = input("Введите список чисел через запятую: ")
    
    numbers = [x.strip() for x in user_input.split(",")]

    result = swap_min_max(numbers)
    
    if isinstance(result, list):
        print("Результат:", result)
    else:
        print(result)

if __name__ == "__main__":
    main()





