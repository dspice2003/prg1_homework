class Irrational:
    
    def _int_(self,iterations):
        self.iterations = iterations
        pass
    
    def _factorial(self,n):
        if n < 1:
            return 1
        else:
            return n * self._factorial(n-1)


print(_factorial(4))

def pi(self,accuracy=1000000):
    pi = 0
    for i in range(1,accuracy):
        pi += ((4.0* (-1)**i)/(2*i-1))
    return pi * -1


def e(places):
    e = 0
    for number in range(0,places):
        e = e + 1/_factorial(number)
    return e

print(e(40))

print(_factorial(4))
print(pi(1000000))    