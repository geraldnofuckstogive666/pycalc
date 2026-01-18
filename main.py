def add(a, b):
    result = a + b
    if result.is_integer():
        return int(result)
    return result

def subtract(a, b):
    result = a - b
    if result.is_integer():
        return int(result)
    return result

def multiply(a, b):
    result = a * b
    if result.is_integer():
        return int(result)
    return result


while True:
    print("\nPersistent Python Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Choose an operation: ")

    if choice == "5":
        print("Calculator closed.")
        break

    if choice in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number. Try again.")
            continue

        if choice == "1":
            print("Result:", add(num1, num2))
        elif choice == "2":
            print("Result:", subtract(num1, num2))
        elif choice == "3":
            print("Result:", multiply(num1, num2))
        else:
            print("Function not implemented yet.")
    else:
        print("Invalid choice. Try again.")
