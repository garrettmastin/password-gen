'''
    Garrett Mastin
    4/25/2023
    program should make passwords
'''

while True:
    start = input("Would you like to make a password? Yes or No\n")
    if start == "yes" or start == "Yes":
        random_yes_no = input("Would you like a random password with high security or a more custom password?")
        if random_yes_no == "yes" or random_yes_no == "Yes":
            print("random")
        elif random_yes_no == "no" or random_yes_no == "No":
            length = input("How many characters long would you like the password to be?")
            special_char_num = input("How many special characters would you like to be in your password?")
            num_uppers = input("How many upper case letters would you like in your password?")
        else:
            try:
                raise TypeError("Input Error")
            except TypeError as te:
                print("Please input a Yes or No")

    elif start == "no" or start == "No":
        print("ok bye")
        exit()

    else:
        try:
            raise TypeError("Input Error")
        except TypeError as te:
            print("Please input a Yes or No")

