##Kavilan Naidoo
##09-01-2015
##swap function

list1 = []
item = "1"
while item!="0":
    item = input("Please enter something you want to add to the list: ")
    if item != "0":
        list1.append(item)

##list1 = ["d","c","b","a"]



no_swaps = False
while no_swaps != True:
    no_swaps = True
    for count in range(len(list1)-1):
        if list1[count] > list1[count+1]:
            no_swaps = False
            temp = list1[count]
            list1[count] = list1[count+1]
            list1[count+1] = temp
print(list1)

    
