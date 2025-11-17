class Calculator:
    """
    Docstring para Calculator
    """

    def __init__(self):
        self.result = "Result:"

    def addition(self, a, b):
        return f"{self.result} {a + b}"

    def subtraction(self, a, b):
        return f"{self.result} {a - b}"

    def multiplication(self, a, b):
        return f"{self.result} {a * b}"

    def divition(self, a, b):
        if b == 0:
            return "Error: Divition for cero"
        return f"{self.result} {a / b}"


class Menu:
    """
    Create menu options
    """

    def __init__(self):
        self.calculadora = Calculator()
        self.opciones = {
            "1": "addition",
            "2": "subtraction",
            "3": "multiplication",
            "4": "divition",
            "5": "close",
        }

    def show_menu(self):
        """show option menu"""
        print("\n--- Menu for calculator ---")
        for key, value in self.opciones.items():
            print(f"{key}. {value}")
        print("-------------------------------")

    def num(self):
        a = int(input("digite numero: "))
        b = int(input("digite numero: "))
        return a, b

    def execute(self):
        while True:
            self.show_menu()
            election = int(input("Selection a options: (1-5): "))

            if election in [1, 2, 3, 4, 5]:
                if election == 1:
                    a, b = self.num()
                    print(self.calculadora.addition(a, b))
                if election == 2:
                    a, b = self.num()
                    print(self.calculadora.subtraction(a, b))
                if election == 3:
                    a, b = self.num()
                    print(self.calculadora.multiplication(a, b))
                if election == 4:
                    a, b = self.num()
                    print(self.calculadora.divition(a, b))
                if election == 5:
                    print(" God bye... ")
                    break


if __name__ == "__main__":
    app_calculator = Menu()
    app_calculator.execute()
