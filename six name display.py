#Kavilan Naidoo
#12-12-2014
#six name display
my_list = []
for count in range(6):
    name = input("please enter a name: ")
    my_list.append(name)
print()

for index,name in enumerate(my_list):
    print("{0}. {1}".format(index+1,name))
print()

which_name=int(input("Which name would you like to view from 1-6? - "))
print()

while which_name >0:
    print(my_list




