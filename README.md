# PasswordStrengthChecker
Console application that accepts user input to determine if password meets minimum requirements and how strong the password is.

## Minimum Requirements:
	>= 8 characters
	lowercase letters
	UPPERCASE LETTERS
	At least one integer
	At least one symbol: ()_$!+=
 
Password strength calculated by [(length + number of integers) * number of special characters]
## Strength scores:
	Score < 15.................Weak Password
	Score between 15 - 24..... Medium Password
	Score >= 24................Strong Password
