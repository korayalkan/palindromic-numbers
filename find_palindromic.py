# Find the palindromic numbers

userInput = int(input('Enter your number: '))
print(f'{userInput} is a Palindromic number!') if str(userInput) == str(userInput)[::-1] else print(f'{userInput} is not a Palindromic number!')