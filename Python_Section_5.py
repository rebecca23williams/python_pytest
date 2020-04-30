name = input("Please enter your name : - ")
age = input("Please enter your age : - ")
location = input("Please enter your location : - ")
print(name + " is " + age + " years old and lives in " + location)

name = input("Please enter your name: ")
math_score = input("Enter your score for Math: ")
science_score = input("Enter your score for Science: ")
english_score = input("Enter your score for English: ")
percentage = (int(math_score) + int(science_score) + int(english_score)) / 3
print(name + " scored " + str(percentage) + "% in the exams")
