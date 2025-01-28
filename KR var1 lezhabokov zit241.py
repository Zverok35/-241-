def print_numbers(A, B):
    for num in range(A, B + 1):
        print(num, end=' ')

# Ввод значений A и B
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

# Проверка условия A ≤ B
if A <= B:
    print("Числа от A до B включительно:")
    print_numbers(A, B)
else:
    print("Ошибка: A должно быть меньше или равно B").
