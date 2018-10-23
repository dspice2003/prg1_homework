'''
problem 1
'''


print("Please enter a number")
number = input(">")
number = int(number)

for factor in range(1,number):
    print(number % factor,factor)
'''
   if(factor % number):
        print(number)
    if(factor == number):
        print(number)
'''        