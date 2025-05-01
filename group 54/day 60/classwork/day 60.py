def main():
    try:
        # ask the user to enter two nums 
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform division
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is {result}")

    except ValueError:
        print("ValueError")

    except ZeroDivisionError:
        print("ZeroDivisionError")

    except :
        print("An unexpected error occurred.")

# Run the program
main()
