
numbers = input("enter 10 numbers with a comma inbetween: ")
# numbers = "1,3,15,16,20,42,2,3,1,4"
print(numbers)
numbers_list = numbers.split(",")
numbers_count = len(numbers_list)
half = int(numbers_count/2)
print(numbers_list)
last_half = numbers_list[half:numbers_count]
print(last_half)
first_half = numbers_list[0:half]
print(first_half)
print(numbers_list[1:9])

reverce_numbers = ",".join(numbers_list[0:numbers_count:-1])
print(reverce_numbers)

print(numbers_list[::-1]) # This code reverces the list

'''
import matplotlib.pylot as plt



xlist = [0,1,2]
ylist = [1,2,4]
x = []



plt.title("y=x**2")
plt.plot(xlist,ylist)
plt.show(xlist,ylist)

'''