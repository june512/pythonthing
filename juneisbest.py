print ("Take this simple test to find out your IQ")
print ("jk")
print ("take this simple test \n")
print ("Who is the best person alive?")

isWrong = True

while isWrong:
    userChoice = input("Your Choice: ")
    if userChoice == "June":
        print ("correct")
        isWrong = False
    elif userChoice == "Jay":
        print ("half credit")
        isWrong = False
        
    else:
        print ("incorrect")
        isWrong = True;
    
print ("Who was our first president?")
userChoice = input("Your Choice:")
if userChoice == "George Washington":
    print ("correct, good job")
else:
    print ("how do you not know this honestly")
    
