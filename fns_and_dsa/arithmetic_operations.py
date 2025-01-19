def perform_operations(num1, num2, operation):
# to perform basic oprtion
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return(num1 - num2)
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Cannot divide by zero"
        else:
         return num1 / num2
    else:
        return "Invalid operation"
