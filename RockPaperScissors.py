import random 

choices = ["rock", "paper", "scissors"]
while is using
while True:
    print("\n--- Rock Paper Scissors Game  ---")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    try:
        user_input = int(input("Enter choice (1-3): "))
        if user_input < 1 or user_input > 3:
            print(" Invalid choice")
            continue
    except:
        print(" Enter a number only")
        continue

    user_choice = choices[user_input - 1]
    computer_choice = random.choice(choices)

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print(" It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("================================")
        
        print(" You win")
    else:
        print("================================")
        print(" Computer wins")

    again = input("\nPlay again? (yes/no): ").lower()
    if again != "yes":
        print(" Thanks for playing")
        break