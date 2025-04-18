class Calculator:
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    def operate(self, operation):
        if operation == "add":
            return self.a + self.b
        elif operation == "subtract":
            return self.a - self.b
        elif operation == "multiply":
            return self.a * self.b
        elif operation == "divide":
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero"
        else:
            return "Invalid operation"

if __name__ == "__main__":
    a = 10  
    b = 5   
    operation = "add"  
    calc = Calculator(a, b)
    
    result = calc.operate(operation)
    print(f"Result of {operation} operation: {result}")
