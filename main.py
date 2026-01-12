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

def calculation (choice, num1, num2):
    if choice == 1:
        return num1+num2
    elif choice == 2:
        return num1-num2
    elif choice == 3:
        return num1*num2
    elif choice == 4:
        if num2 == 0:
            return "Error: Division by zero"
        return num1/num2
    else:
        return "invalid operation"
    
def main():
    while True:
        show_menu()
        choice = int(input("Enter your choice(1-5): "))
        if choice == 5:
            print("Exiting calculator. Goodbye!")
            break

        num1, num2 = get_number()
        if num1 is None:
            continue

        result = calculation(choice,num1, num2)
        print("Result: ",result)

if __name__ == "__main__":
    main()

    
     