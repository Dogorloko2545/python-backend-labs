class Calculator:
    """
    Docstring para Calculator
    """

    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def message(self):
        return "Resultado: "

    def addition(self):
        return f"{self.message()} {self.a + self.b}"

    def subtraction(self):
        return f"{self.message()} {self.a - self.b}"

    def multiplication(self):
        return f"{self.message()} {self.a * self.b}"

    def divition(self):
        if self.b == 0:
            return "Error: Divition for cero"
        return f"{self.message()} {self.a / self.b}"


class Menu(Calculator):
    """
    Create menu options
    """

    def __init__(self):
        # self.calculadora = Calculator()
        super().__init__()
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

    def number(self):
        self.a = int(input("enter number: "))
        self.b = int(input("enter number: "))

    def execute(self):
        while True:
            self.show_menu()
            election = int(input("Selection a options: (1-5): "))

            match election:
                case 1:
                    self.number()
                    print(self.addition())
                case 2:
                    self.number()
                    print(self.subtraction())
                case 3:
                    self.number()
                    print(self.multiplication())
                case 4:
                    self.number()
                    print(self.divition())
                case 5:
                    break
                case _:
                    print("Selection a options...")


if __name__ == "__main__":
    app_calculator = Menu()
    app_calculator.execute()
