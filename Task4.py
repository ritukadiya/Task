#Calculator Program
def calculator():
    
    try:
        n1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /, %): ")
        n2 = float(input("Enter the second number: "))

        if operator == "+":
            result = n1 + n2
        elif operator == "-":
            result = n1 - n2
        elif operator == "*":
            result = n1 * n2
        elif operator == "/":
            if n2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = n1 / n2
        elif operator == "%":
            if n2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = n1 % n2
        else:
            print("Invalid operator.Use one of the following: +, -, *, /, %")
            return

        print(f"The result of {n1} {operator} {n2} is: {result}")
    except ValueError:
        print("Invalid input. Enter numerical values.")

calculator()
