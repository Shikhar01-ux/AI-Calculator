def show_menu():
    print("------AI CALCULATOR------")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. EXIT")

def get_number():
    try:
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        return num1, num2
    except ValueError:
        print("Invalid input! please return number only.")
        return None, None
     