"""
    6.29
    Write a program that prompts the user to enter a credit number
    cards as an integer. Display whether the number is valid or invalid.
    author Kalugin Alexander
    email sashakalugin74@gmail.com
    version 3.11 02/12/23
    group 10701223

"""

# Return this number if it is a single digit, otherwise,
# return the sum of the two digits
def getDigit(number):
    if number < 10:
        a = number
    else:
        a = number % 10 + number // 10
    return a

# Number of digits in the card
def getSize(number):
    d = len(str(number))
    return d

# Card type determination
def getPrefix(number):
    a = str(number)
    if a[0] == "4":
        k = "Visa"
    elif a[0] == "5":
        k = "MasterCard"
    elif a[0] == "3" and a[1] == "7":
        k = "American Express"
    elif a[0] == "6":
        k = "Discover"
    else:
        k = "Another type of card"
    return k

# Sum of even numbers from the end
def sumOfDoubleEvenPlace(number):
    sum = 0
    a = str(number)
    i = getSize(number) - 2
    while i >= 0:
        sum += getDigit(int(a[i]) * 2)
        i -= 2
    return sum

# Sum of odd numbers from the end
def sumOfOddPlace(number):
    sum = 0
    a = str(number)
    i = getSize(number) - 1
    while i >= 0:
        sum += int(a[i])
        i -= 2
    return sum

# Checking the validity of the card
def isValid(number):
    valid = False
    if 13 <= getSize(number) <= 16:
        a = sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)
        if a % 10 == 0:
            valid = True
    return valid

num = int(input("Enter the card number: "))
if isValid(num):
    print("Card is valid")
else:
    print("Card is not valid")
print("Type of card:", getPrefix(num))