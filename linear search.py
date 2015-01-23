#Kavilan Naidoo
#09-01-2015
#Linear Search


def input_():
    list1 = []
    item = "1"
    while item!="0":
        item = input("Please enter something you want to add to the list: ")
        list1.append(item)
    item_search = input("Please enter an item you want to search for: ")
    return item_search , list1



def linear_search(list1, item_search):
    found = False
    count = 0
    while not found and count<len(list1):
        if list1[count] == item_search:
            print("Found")
            found = True
        else:
            print("Not found")
        count = count + 1
   

def main():
    
    item_search,list1 =input_()
    linear_search(list1, item_search)
main()

    
