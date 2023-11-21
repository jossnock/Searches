def linear_search(search_item, array):
    """searches through an unordered linear array for a number linearly
    returns item's position if it's in the list
    returns -1 if the item isn't in the list"""
    for position in range(len(array)):
        if array[position] == search_item: #tests if an item is the search item
            return position
    return -1 #triggers if the entire array is searched and the item isn't found


def binary_search(search_item, array):
    """searches through an ordered (small to large) linear array for a number
    returns item's position if it's in the list
    returns -1 if the item isn't in the list"""
    #defining variables
    item_found = False
    array_start = 0
    array_end = len(array) - 1
    while array_start <= array_end and item_found == False:
        array_midpoint = (array_start + array_end) // 2
        if array[array_midpoint] == search_item: #tests if an item is the search item
            item_found = True
        else:
            if array[array_midpoint] < search_item: #if the item is after the midpoint, the midpoint is the new start
                array_start = array_midpoint + 1
            else:
                array_end = array_midpoint - 1 #if the item is after the midpoint, the midpoint is the new end
    if item_found == True:
        return array_midpoint
    else: #if the item isn't in the list, return -1
        return -1


def binary_search_recursive(search_item, array, array_start, array_end):
    """searches through an ordered (small to large) linear array for a number recursively
    returns item's position if it's in the list
    returns -1 if the item isn't in the list"""
    #base cases
    if array_start > array_end:
        return -1
    array_midpoint = (array_start + array_end) // 2
    current_item = array[array_midpoint]
    if current_item == search_item:
        return array_midpoint
    elif current_item < search_item:
        return binary_search_recursive(search_item, array, array_midpoint + 1, array_end)
    else:
        return binary_search_recursive(search_item, array, array_start, array_midpoint - 1)


#tests
my_array = [1,2,3,4,6,7,9,13,15,18,25,28,35,36,39,56,83]

print(linear_search(7,my_array))
print(binary_search(7,my_array))
print(binary_search_recursive(7,my_array, 0, 16))