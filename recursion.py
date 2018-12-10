'''


def countup(count=1):
    if(count>10):
        return
    else:
        print(count)
        return countup(count + 1)
    pass


countup()

'''

'''
def countdown(count=10):
    if(count<0):
        return
    else:
        print(count)
        return countdown(count - 1)
    pass

countdown()
'''

'''
def simple_bunny_ears(bunnies):
    if(bunnies == 0):
        return 0
    else:
        return 2 + simple_bunny_ears(bunnies - 1)
print(simple_bunny_ears(6))
'''

def complex_bunny_ears(bunnies):
    if(bunnies == 0 ):
        return 0
    elif(bunnies % 2 == 0 ):
        return 2 + complex_bunny_ears(bunnies - 10)
    else:
        return 3 + complex_bunny_ears(bunnies - 1)

print(complex_bunny_ears(3))