from complex_numbers.complex_number import ComplexNumber

class Operations:
    @staticmethod
    def add(num1, num2):
        real = num1.real + num2.real
        imaginary = num1.imaginary + num2.imaginary
        return ComplexNumber(real, imaginary)

    @staticmethod
    def multiply(num1, num2):
        real = num1.real * num2.real - num1.imaginary * num2.imaginary
        imaginary = num1.real * num2.imaginary + num1.imaginary * num2.real
        return ComplexNumber(real, imaginary)

    @staticmethod
    def divide(num1, num2):
        denominator = num2.real**2 + num2.imaginary**2
        real = (num1.real * num2.real + num1.imaginary * num2.imaginary) / denominator
        imaginary = (num2.real * num1.imaginary - num1.real * num2.imaginary) / denominator
        return ComplexNumber(real, imaginary)
