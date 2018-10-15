
'''
a strong number is defined as a number that has the sum of the factorial of
 each digit is egual to its original number

 '''

#get all of the digits (split)
for number_to_check in range(10000001):
    snumber = str(number_to_check)


    digits = list(snumber)

    sum = []
    #calculate factorial for each digit
    for digit in digits:
        factorial = 1
        for number in range(1,int(digit)+ 1):
            factorial = number * factorial
        sum.append(factorial)



    final_factorial = 0
    for number in sum:
        final_factorial += number
    print(final_factorial)


    final_factorial = str

    if (final_factorial == snumber):
        print(snumber,"This number is strong")