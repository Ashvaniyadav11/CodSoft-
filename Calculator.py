def calculator():
    #this calculator work on Arithmetic operation
    while True:
        try:
            # taking input from user
            num1 = float(input("\nEnter first number  : "))
            num2 = float(input("Enter second number  : "))
            
            # Displaying Operation
            print("\nSelect operation:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")
            print("5. Exit")
            
            choice = input("\nEnter  your choice (1-5): ")
            
            # performing calculation
            if choice == '1':
                result = num1 + num2
                print(f"\n{num1} + {num2} = {result}")
            
            elif choice == '2':
                result = num1 - num2
                print(f"\n{num1} - {num2} = {result}")
            
            elif choice == '3':
                result = num1 * num2
                print(f"\n{num1} * {num2} = {result}")
            
            elif choice == '4':
                if num2 != 0:
                    result = num1 / num2
                    print(f"\n{num1} / {num2} = {result}")
                else:
                    print("\n Error: Division by zero is not allowed!")
            
            elif choice == '5':
                print("\n Thanks for using my calculator")
                break
            
            else:
                print("\n Invalid choice  select in between 1-5.")
            
            # Ask if user wants to continue
            continue_choice = input("\nDo you want to extra Calculation (yes/no): ")
            if continue_choice.lower() not in ['yes', 'y']:
                print("\n Thanks for using my calculator")
                break
        
        except ValueError:
            print("\n Error: Please enter valid numbers!")
        except Exception as e:
            print(f"\n An error occurred: {e}")

if __name__ == "__main__":
    calculator()