# Take a number from the user
number = input("Please enter a number: ")
number = int(number)

if number >= 0:
    if number % 2 == 0:
        print("This is an even number")
    else:
        print("This is an odd number")
else:
    print("This is a negative number")
