#calculator
def addition(num1,num2):
    return num1 + num2

def subtraction(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    return num1 / num2
def calculator():
    print("Select operation.")
    print("1.Addition")      
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    while True:
        choice = input("Enter choice(1/2/3/4/5): ")
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if choice == '1':
                print(num1, "+", num2, "=", addition(num1, num2))
            elif choice == '2':
                print(num1, "-", num2, "=", subtraction(num1, num2))
            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))
            elif choice == '4':
                if num2 != 0:
                    print(num1, "/", num2, "=", divide(num1, num2))
                else:
                    print("Error! Division by zero is not possible.")
        elif choice == '5':
            print("Exiting the calculator.")
            break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    print("Calculator")
    calculator()