print("*****************")
print("Challenges 105")
file = open("Numbers.txt","w")
file.write("4, ")
file.write("6, ")
file.write("10, ")
file.write("8, ")
file.write("5, ")
file.close()

print("*****************")
print("Challenges 106")
file = open("Names.txt","w")
file.write("Bob\n")
file.write("Tom\n")
file.write("Gemma\n")
file.write("Sarah\n")
file.write("Timothy\n")
file.close()

print("*****************")
print("Challenges 107")
file = open("Names.txt","r")
print(file.read())
file.close()

print("*****************")
print("Challenges 108")
file = open("Names.txt","a")
newname = input("Enter a new name: ")
file.write(newname + "\n")
file.close

file = open("Names.txt","r")
print(file.read())
file.close

print("*****************")
print("Challenges 109")
print ("1) Create a new file")
print ("2) Display the file")
print ("3) Add a new item to the file")
selection = int(input("Make a selection 1, 2 or 3: "))
if selection == 1:
    subject = input("Enter a school subject: ")
    file = open("Subject.txt","w")
    file.write(subject + "\n")
    file.close()
elif selection == 2:
    file = open("Subject.txt","r")
    print(file.read())
elif selection == 3:
    file = open("Subject.txt","a")
    subject = input("Enter a school subject: ")
    file.write(subject + "\n")
    file.close()
    file = open("Subject.text","r")
    print(file.read())
else:
    print("Invalid option")

print("*****************")
print("Challenges 110")
file = open("Names.txt","r")
print(file.read())
file.close()

file = open("Names.txt","r")
selectedname = input("Enter a name from the list: ")
selectedname = selectedname + "\n"
for row in file:
    if row != selectedname:
        file = open("Names2.txt","a")
        newrecord = row
        file.write(newrecord)
        file.close()
file.close()