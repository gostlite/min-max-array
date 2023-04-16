from functools import reduce

def min_max(arr):
    arr.sort()
    # Calculate the minimum value by summing the four smallest integers
    min_value = sum(arr[:4])
    # Calculate the maximum value by summing the four largest integers
    max_value = sum(arr[-4:])
    print( min_value, max_value)
    
    
    
def minMAxSum(arr):
    min_value= min(arr)
    max_value = max(arr)
    red = reduce
    min_array = [k for k in arr if not k == min_value]
    max_array = [k for k in arr if not k == max_value]
    total_for_min_arr = red(lambda a,b:a+b, min_array)
    total_for_max_arr = red(lambda a,b:a+b, max_array)
    print(total_for_max_arr, total_for_min_arr)
