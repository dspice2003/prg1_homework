# This program prints the largest number


number = input(" Enter numbers with a space: ")
numbers_list = number.split(" ")

max_number = int(numbers_list[0])

for number in numbers_list:
    int_number = int(number)
    if(max_number < int_number):
        max_number = int_number
print("The largest number is ",max_number)