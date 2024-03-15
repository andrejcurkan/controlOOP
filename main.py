from user_interaction.user_interaction import get_complex_number_from_user, get_operation_from_user
from complex_numbers.complex_number import ComplexNumber
from calculator.calculator import Calculator
from logging_utils.logger import logger

if __name__ == "__main__":
    num1 = get_complex_number_from_user()
    num2 = get_complex_number_from_user()
    operation = get_operation_from_user()

    calculator = Calculator()

    if operation == '+':
        result = calculator.add(num1, num2)
    elif operation == '*':
        result = calculator.multiply(num1, num2)
    elif operation == '/':
        result = calculator.divide(num1, num2)

    logger.info(f"{num1} {operation} {num2} = {result}")
