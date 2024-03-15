def validate_real_number_input(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Ошибка: Введите действительное число.")

def validate_complex_number_input():
    real = validate_real_number_input("Введите действительную часть комплексного числа: ")
    imaginary = validate_real_number_input("Введите мнимую часть комплексного числа: ")
    return real, imaginary

def validate_operation_input():
    while True:
        operation = input("Введите операцию (+, *, /): ")
        if operation in ('+', '*', '/'):
            return operation
        else:
            print("Неверная операция. Пожалуйста, введите '+', '*' или '/'.")
