def main():

    MIN_LENGTH = 8
    password = input("Enter your password: ")
    if len(password) >= MIN_LENGTH:
        print('*' * len(password))
    else:
        print(f"Password must be at least {MIN_LENGTH} characters long.")

main()