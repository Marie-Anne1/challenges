print("*******************")
print("Challenges 045")
total = 0
while total <= 50:
    num = int(input("Enter a number: "))
    total = total + num
    print("The total is...", total)
print()

print("*******************")
print("Challenges 046")
num = 0 
while num <= 5:
    num = int(input("Enter a number: "))
    print("The last number you entered was", num)
print()

print("*******************")        
print("Challenges 047")    
num1 = int(input("Enter a number: "))
total = num1
again = "y"
while again == "y":
    num2 = int(input("Enter another number: "))
    total = total + num2
    again = input("Do you want to add another number? (y/n) ")
print("The total is", total)    
print()

print("********************")
print("Challenges 048")
again = "y"
count = 0
while again == "y":
    name = input("Enter a name of sombody you want to invite to your party: ")
    print(name, "has now been invited")
    count = count + 1
    again = input("Do you want to invite somebody else? (y/n) ")
print("You have", count, "People coming to your party")   
print()

print("*********************")
print("Challenges 049")
compnum = 50
guess = int(input("Can you guess the number I am thinking of? "))
count = 1
while guess != compnum:
    if guess < compnum:
        print("Too low")
    else:
        print("Too high")
    count = count+1
    guess = int(input("Have another guess: "))
print("Well done, you took", count, "attempts") 
print()

print("******************")
print("Challenges 050")
num = int(input("Enter a number between 10 and 20: "))
while num <10 or num>20:
    if num <10:
        print("Too low")
    else:
        print("Too high")
    num = int(input("Try again: "))  
print("Thank you")    
print()

print("********************")
print("Challenges 051")
num = 10
while num >0:
    print("There are ", num, "green bottles hanging on the well.")
    print(num, "green bottles hanging on the wall.")
    print("And if I green bottle should accidentally fall,")
    num = num - 1
    answer = int(input("How many green bottles will be hanging on the wall? "))
    if answer == num:
        print("There will be", num, "green bottles hanging on the wall.")
    else:
        while answer!=num:
            answer = int(input("No, try again: "))
print("There are no more green bottles hanging on the wall.")