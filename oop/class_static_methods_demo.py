import calculator
class Calculator:
    calculation_type = "Arithmetic Operations"
    @staticmethod
    def add(a, b):
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        return a * b

    print(f"Calculation Type: {cls.calculation_type})
        

