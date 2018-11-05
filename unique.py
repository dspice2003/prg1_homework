'''
function name: make_unique
parameters: list
returns: list
'''

def make_unique(values):
    unique = []
    for value in values:
        if(not value in unique):
        unique.append(value)
    return unique

# Or print(make_unique)(input("Enter values seperated by a comma ").split(",")))

list_values = input("Please enter a number seperated by a comma: ").split(",")
print(list_values)
make_unique(list_values)