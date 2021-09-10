print("******************")
print("Challenges 001")
firstname = input("Enter your first name: ")
print("Hello",firstname)
print()

print("******************")
print("Challenges 002")
firstname = input("Enter your first name: ")
surname = input("Enter your surname: ")
print("Hello",firstname, surname)
print()

print("******************")
print("Challenges 003")
print("What do you call a bear with no teeth?\nA gummy bear!")
print()

print("******************")
print("Challenges 004")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
answer = num1 + num2
print("The answer is", answer)
print()

print("*******************")
print("Challenges 005")
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
num3 = int(input("Enter your Third number: "))
answer = (num1 + num2) * num3
print("The answer is", answer)
print()

print("*******************")
print("Challenges 006")
startNum = int(input("Enter the number of slices of pizza you started with: "))
endNum = int(input("How many slices have you eaten? "))
slicesLeft = startNum - endNum
print("You have", slicesLeft, "slices remaining")
print()

print("********************")
print("Challenges 007")
name = input("What is your name? ")
age = int(input("How old are you? "))
newAge = age + 1
print(name, "next birthday you will be", newAge)
print()

print("*********************")
print("Challenges 008")
bill = int(input("What is the total cost of the bill? "))
people = int(input("How many people are there? "))
each = bill/people
print("Each person should pay", each)
print()

print("*********************")
print("Challenges 009")
days = int(input("Enter the number of days: "))
hours = days*24
minutes = hours*60
seconds = minutes*60
print("In", days,"days there are...")
print(hours, "hours")
print(minutes, "minutes")
print(seconds, "seconds")
print()

print("*******************")
print("Challenges 010")
kilo = int(input("Enter the number of kilos: "))
pound = kilo * 2.204
print("That is", pound,"pounds")
print()

print("*******************")
print("Challenges 011")
larger = int(input("Enter the number over 100: "))
smaller = int(input("Enter a number under 10: "))
answer = larger//smaller
print(smaller,"goes into", larger, answer,"times")