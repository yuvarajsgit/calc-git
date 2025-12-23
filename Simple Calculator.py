#Simple Calculator Program

# Taking input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Display operations
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Exponent")

choice = input("Enter the Choice: ")

# Performing calculation
if choice == '1':
    print("Result:", num1 + num2)

elif choice == '2':
    print("Result:", num1 - num2)

elif choice == '3':
    print("Result:", num1 * num2)

elif choice == '4':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero")
elif choice == '5':
    print("Result:", num1 % num2)
    
elif choice == '6':
    print("Result:", num1 * num2)

else:
    print("Invalid choice")
