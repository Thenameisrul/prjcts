import random
print("Welcome to the PyPassword Generator!")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = letters + numbers + symbols
user_choice = int(input("You want a password suggestion? Type 0 for yes, 1 for no.\n"))

if user_choice == 1:
    password_length = int(input("Length of your password:"))
    rand_password = random.sample(password, password_length)
    passwords = ""
    for pass_w in rand_password:
        passwords += pass_w
    print(f"Your password is: {passwords}")


elif user_choice == 0:
    print("Create Your own password.\n")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    password_list = []
    for char in range(0, nr_letters):
        password_list.append(random.choice(letters))

    for char in range(0, nr_symbols):
        password_list.append(random.choice(symbols))

    for char in range(0, nr_numbers):
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    print(f"Your password is: {password}")
else:
    print("Wrong Input")

