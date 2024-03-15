from complex_numbers.complex_number import ComplexNumber

class ComplexNumberFactory:
    @staticmethod
    def create_complex_number(real, imaginary):
        return ComplexNumber(real, imaginary)
