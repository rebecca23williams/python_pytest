x = int(input("Enter a number: "))

number = 0
for i in range(2, x):
    if x % i == 0:
        print("This is not a prime number")
        number = 1
        break
    i = i + 1
if number == 0:
    print("This is a prime number")
