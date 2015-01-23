def initialise_frequency_array():
    array = []
    return array

def simulate_die_throwing(array):
    import random
    for count in range(6):
        number = random.randint(1,6)
        array.append(number)
    return array

def display_result_array(array,number):
    count = 0
    count1 = 0
    print("{0:^2} {1:^2}".format("Score","Frequency"))
    for each in array:
        print("{0:>3} {1:>7}".format(count+1,array[count1]))
        count = count+1
        count1=count1+1

def Frequency_of_die_score():
    array = initialise_frequency_array()
    number = simulate_die_throwing(array)
    display_result_array(array,number)

Frequency_of_die_score()
