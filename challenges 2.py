print("*****************")
print("Challenges 012")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
    print(num2, num1)
else:
    print(num1, num2)
print()

print("*****************")
print("Challenges 013")
num = int(input("Enter a number that is under 20: "))
if num >= 20:
    print("Too high")
else:
    print("Thank you")
print()

print("*****************")
print("Challenges 014")
num = int(input("Enter a number between 10 and 20: "))
if num >= 10 and num <= 20:
    print("Thank you")
else:
    print("Incorrect answer")
print()

print("*****************")
print("Challenges 015")
color = input("Enter your favorite color: ")
if color == "red" or color == "RED" or color == "Red":
    print("I like red too")
else:
    print("I don't like this color, I prefer red.")
print()

print("*****************")
print("Challenges 016")
raining = input("Is it raining?")
raining = str.lower(raining)
if raining == "yes":
    windy = input("Is it windy?")
    windy = str.lower(windy)
    if windy == "yes":
        print("It is too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy your day")
print()

print("*****************")
print("Challenges 017")
age = int(input("What old are you?: "))
if age >= 18:
    print("You can vote")
elif age == 17:
    print("You can learn to drive")
elif age == 16:  
    print("You can buy a lottery ticket")
elif age <= 16:
    print("You can go Trick-or-Treating") 
print()

print("*****************")
print("Challenges 018")
num = int(input("Enter a number: "))
if num <= 10:
    print("Too low")
elif num >= 10 and num <= 20:
    print("correct")
else:
    print("Too high")
print()

print("*****************")
print("Challenges 019")
num = int(input("Enter 1,2 or 3: "))
if num == "1":
    print("Thank you")
elif num == "2":
    print("Well done")
elif num == "3":
    print("Correct")
else:
    print("Error message")