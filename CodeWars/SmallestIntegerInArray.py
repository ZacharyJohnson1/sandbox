'''
Given an array of integers your solution should find the smallest integer.
For example:
Given [34, 15, 88, 2] your solution will return 2
Given [34, -345, -1, 100] your solution will return -345
You can assume, for the purpose of this kata, that the supplied array will not be empty.
'''

def find_smallest_int(arr):
    
    min = arr[0]
    for element in range(1, len(arr)):
        if min > arr[element]:
            min = arr[element]
    return min

print(find_smallest_int([3,7,1,5,-2,9]))
print(find_smallest_int([8,2,3,5,6,0]))