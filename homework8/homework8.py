import random

def get_user_numbers(num_count, num_range):
    user_numbers = set()
    print(f"Выберите {num_count} уникальных чисел от 1 до {num_range}:")
    while len(user_numbers) < num_count:
        try:
            number = int(input(f"Введите число {len(user_numbers) + 1}: "))
            if number < 1 or number > num_range:
                print(f"Ошибка: число должно быть в диапазоне от 1 до {num_range}.")
            elif number in user_numbers:
                print("Ошибка: число уже выбрано. Выберите другое.")
            else:
                user_numbers.add(number)
        except ValueError:
            print("Ошибка: введите целое число.")
    return user_numbers

def generate_random_numbers(num_count, num_range):
    return set(random.sample(range(1, num_range + 1), num_count))

def display_results(user_numbers, program_numbers):
    print("nВаши числа:", sorted(user_numbers))
    print("Числа программы:", sorted(program_numbers))
    
    matches = user_numbers.intersection(program_numbers)
    print(f"nСовпадения: {sorted(matches)}")
    print(f"Количество совпадений: {len(matches)}")

def main():
    num_count = 5  # Количество чисел для выбора
    num_range = 25  # Диапазон чисел (от 1 до num_range)
    
    user_numbers = get_user_numbers(num_count, num_range)
    program_numbers = generate_random_numbers(num_count, num_range)
    
    display_results(user_numbers, program_numbers)

if __name__ == "__main__":
    main()

