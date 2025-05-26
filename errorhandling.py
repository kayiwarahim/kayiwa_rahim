while True:
    try:
       
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        
        result = num1 / num2

    except ValueError:
        print("Invalid input! Please enter numeric values only.")
    except ZeroDivisionError:
        print("Division by zero is not allowed. Please enter a non-zero second number.")
    else:
        print(f"The result of {num1} divided by {num2} is: {result}")
        break