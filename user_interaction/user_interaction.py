from complex_numbers.complex_number import ComplexNumber

from input_validation.input_validation import validate_complex_number_input, validate_operation_input

def get_complex_number_from_user():
    real, imaginary = validate_complex_number_input()
    return ComplexNumber(real, imaginary)

def get_operation_from_user():
    return validate_operation_input()
