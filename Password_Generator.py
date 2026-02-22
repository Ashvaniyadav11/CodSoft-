import random
import string


def password_generator():
    print("="*20)
    print("PASSWORD GENERATOR")
    print("="*20)
    
    while True:
        try:
            # to get validation password length
            length_input = input("Enter Password length (6-18): ")
            length = int(length_input)
            
            # Checking length for valid range
            if length < 6:
                print("Password too short, Minimum length is 6.")
                continue
            elif length > 20:
                print(" Password too long, Maximum length is 18.")
                continue
            else:
                break  # valid input then exit the Loop
                
        except ValueError:
            print(f"Invalid input! '{length_input}' is not a number. Enter a number between 6-20.")
    
    # Character sets
    lowercase = string.ascii_lowercase      # a-z
    uppercase = string.ascii_uppercase      # A-Z
    digits = string.digits                   # 0-9
    symbols = "!@#$%^&*"                     # Special characters
    
    # Combining all characters
    all_chars = lowercase + uppercase + digits + symbols
    
    # Generating password
    password = []
    
    # At least one character from each
    password.append(random.choice(lowercase))
    password.append(random.choice(uppercase))
    password.append(random.choice(digits))
    password.append(random.choice(symbols))
    
    # Generating password
    for _ in range(length - 4):
        password.append(random.choice(all_chars))
    
    # Shuffling the password
    random.shuffle(password)
    
    # Convert list to string
    final_password = ''.join(password)
    
    print("\n" + "="*40)
    print(f" Generated Password: {final_password}")
    print(f" Password Length: {length}")
    print("="*40)


if __name__ == "__main__":
    password_generator()