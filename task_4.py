def sum(x, y):
    return x + y


def subtract(x, y):
    return x - y


def product(x, y):
    return x * y


def division(x, y):
    return x / y

while True:
    
    number_1 = input("Enter first number: ")
    
    choice = input("Enter choice(+ | - | * /): ")

    if choice in ('+', '-', '*', '/'):
        num1 = float(number_1)
        num2 = float(input("Enter second number: "))

        if choice == '+':
            print(num1, "+", num2, "=", sum(num1, num2))

        elif choice == '-':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '*':
            print(num1, "*", num2, "=", product(num1, num2))

        elif choice == '/' and num2 != 0:
            print(num1, "/", num2, "=", division(num1, num2))
        
        else:
            print("Devision by 0")
        
        next_calculation = input("Retry? (y/n): ")
        if next_calculation == "n":
            break
    
    else:
        print("Invalid Input")