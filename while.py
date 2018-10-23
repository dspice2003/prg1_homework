x = 0

times = int(input("how many times would you like to loop: "))
stars = ""
y = 0
while(y < times):
    stars += ""
    x = 0
    while(x < times):
        stars += "*"
        x = x + 1
    print(stars)
    y += 1
    