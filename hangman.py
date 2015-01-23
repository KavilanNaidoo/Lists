#Kavilan Naidoo
#16-01-2015
#hangman


string = input("please enter a string: ")
character = input("please enter a character to search for: ")



count = 0
while count<len(string):
    if string[count] ==character:
        print(character)
    
    else:
        print("-")
    count = count + 1
        
