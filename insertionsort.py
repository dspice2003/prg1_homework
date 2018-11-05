def find_minimum_value(values):
    special_value = values[0]
    
    for value in values:
        if(value < special_value):
            special_value = value
    return special_value

def insertion_sort(values):

    while(len(values)>0):
        smallest = find_minimum_value(values)
        values.remove(smallest)
        smallest_list.append(smallest)

    unsorted = [9,4,94,56,2,14]
    sorted = insertion_sort(unsorted)
    print(sorted)