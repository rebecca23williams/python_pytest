# Check number is divisible by 5 and 11
number = input("Please enter a number")

if int(number) % 5 == 0 and int(number) % 11 == 0:
    print("Number is divisible by both 5 and 11")
elif int(number) % 5 == 0:
    print("Number is only divisible by 5")
elif int(number) % 11 == 0:
    print("Number is only divisible by 11")
else:
    print("Number is not divisible by 5 or 11")