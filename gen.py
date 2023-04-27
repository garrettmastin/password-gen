import random
import array


def random_pass():  # function that makes a random password
    max_num = input("What would  you like the max length of the password to be?")
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                 'z']

    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                 'Z']

    symbols = ['@', '#', '$', '%', '=', ':', '?', '.',
               '/', '|', '~', '>', '*', '(', ')', '<']

    combined_array = digits + uppercase + lowercase + symbols

    random_digit = random.choice(digits)
    random_lower = random.choice(lowercase)
    random_upper = random.choice(uppercase)
    random_symbol = random.choice(symbols)

    temp = random_digit + random_lower + random_upper + random_symbol

    for x in range(int(max_num) - 4):
        temp = temp + random.choice(combined_array)
        temp_pass_list = array.array('u', temp)
        random.shuffle(temp_pass_list)

    password = ""
    for x in temp_pass_list:
        password = password + x

    print("Your password is: {}".format(password))


# main part of the program
while True:  # while loop that makes the program run until the user is done
    start = input("Would you like to make a password? Yes or No\n")
    if start == "yes" or start == "Yes":
        while True:
            random_yes_no = input("Would you like a random password with high security?")
            if random_yes_no == "Yes" or random_yes_no == "yes":
                random_pass()
                exit()
            elif random_yes_no == "No" or random_yes_no == "no":
                print("ok bye")
                exit()
            else:
                # raises a typer error if the if else block doesn't catch the input from the user
                # then restarts the loop for the user to try again
                raise TypeError("Input Error")
    elif start == "no" or start == "No":
        print("ok bye")
        exit()
    else:
        # raises a typer error if the if else block doesn't catch the input from the user
        # then restarts the loop for the user to try again
        raise TypeError("Type Error")
        break


