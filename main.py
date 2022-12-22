
# Password Strength Checker Considerations

# Minimum Requirements:
#   >= 8 characters
#   lowercase letters
#   UPPERCASE LETTERS
#   At least one integer
#   At least one symbol: ()_$!+=

#   Password strength calculated by [(length + number of integers) * number of special characters]

import re

flag = 0
errorMessage = ""

# This checks bare minimum requirements
def try_pass(pwd, errorMessage=None):
    print(pwd)

    while True:

        if len(pwd)<8:
            errorMessage = "Password too short. "
            flag = -1
            break

        elif not re.search('[a-z]', pwd):
            errorMessage = "Password must contain at least one lowercase letter. "
            flag = -1
            break

        elif not re.search('[A-Z]', pwd):
            errorMessage = "Password must contain at least one uppercase letter. "
            flag = -1
            break

        elif not re.search('[0-9]', pwd):
            errorMessage = "Password must contain at least one number. "
            flag = -1
            break

        elif not re.search("[=$@!&_{}~]", pwd):
            errorMessage = "Password must contain at least one of the select symbols =$@!&_{}~"
            flag = -1
            break

        else:
            flag = 0
            break

    if flag == -1:
        print("Password not valid: " + errorMessage)
    else:
        print("Gr8 password M8!")
        strength_check(pwd)

# This checks overall strength of password if it is valid.
def strength_check(pwd):
    print("testing passing to strength_check " + pwd)
    strength_score = 0
    pwd_length = len(pwd)
    letter_count = 0
    num_count = 0
    space_count = 0
    special_count = 0

    for i in pwd:
        if i.isalpha():
            letter_count += 1
        elif i.isnumeric():
            num_count += 1
        elif i.isspace():
            space_count += 1
        else:
            special_count += 1

    strength_score = (pwd_length + num_count) * special_count

    if strength_score < 15:
        print("Weak password, but I'll allow it.")

    elif 15 <= strength_score <= 24:
        print("Decent password.")

    elif strength_score > 24:
        print("GR8 password M8!")


pwd = input("Enter your password")
try_pass(pwd, errorMessage)






