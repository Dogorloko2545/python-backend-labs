class Calculator:
    """
    Docstring para Calculator
    """

    def __init__(self):
        pass

    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def divition(self, a, b):
        if b == 0:
            return "Error: Divition for cero"
        return a / b
