num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
calculator = input("Choose the operation (+, -, *, /): ")
match calculator:
    case'+':
        result = (num1 + num2)
        print("The result is", result)
    case'-':
        result = (num1 - num2)
        print("The result is", result)
    case'*':
        result = (num1 * num2)
        print("The reult is", result)
    case'/':
        if  num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = (num1 / num2)
            print("The result is", result)
    case _: 
        print("Invalid operation")
