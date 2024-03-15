from operations.operations import Operations

class Calculator:
    @staticmethod
    def add(num1, num2):
        return Operations.add(num1, num2)

    @staticmethod
    def multiply(num1, num2):
        return Operations.multiply(num1, num2)

    @staticmethod
    def divide(num1, num2):
        return Operations.divide(num1, num2)
