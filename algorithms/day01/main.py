
## TODO: Print all the integers from 1 to 255.
def print_1_to_255():
    for i in range(1, 256):
        print(i)

# print_1_to_255()
## TODO: Print integers from 0 to 255, and with each integer print the sum so far.
def print_ints_and_sum_0_to_255():
    sum = 0
    for i in range(256):
        sum += i
        print(i, sum)

# print_ints_and_sum_0_to_255()
## TODO: Given an array, find and print its largest element.
def print_max_of_array(arr):
    max = 0
    for i in arr:
        if max < i:
            max = i
    print(max)

# print_max_of_array([1,2,3,4,5,42,6,7,9])

## TODO: Create an array with all the odd integers between 1 and 255 (inclusive).
def return_odds_array_1_to_255():
    new_list = []
    for i in range(1, 256, 2):
        new_list.append(i)
    return new_list

# print(return_odds_array_1_to_255())
## TODO: Given an array and a value Y, count and print the number of array values greater than Y.
def return_array_count_greater_thanY(arr, y):
    count = 0
    for i in arr:
        if i > y:
            count += 1
    print(count)

# ! TEST:
# return_array_count_greater_thanY([23, 45, 67, 12, 42], 20)
# return_array_count_greater_thanY(return_odds_array_1_to_255(), 163)
## TODO: Given an array, print the max, min and average values for that array.
def printMaxMin_average_array_vals(arr):
    max = arr[0]
    min = arr[0]
    sum = 0
    for i in arr:
        if max < i:
            max = i
        if min > i:
            min = i
        sum += i
    print(max)
    print(min)
    print(sum/len(arr))
    

# printMaxMin_average_array_vals([1,2,3,4,5,6])
## TODO: Replace any negative array values with 'Dojo'.
def swapStringFor_array_negative_vals(arr):
    new_list = []
    for i in arr:
        if i < 0:
            i = "Dojo"
        new_list.append(i)
        print(i)
    return new_list

# print(swapStringFor_array_negative_vals([-1, 4, -5, 67, -55, 42]))
def swapStringFor_array_negative_vals2(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = "Dojo"
    return arr

# print(swapStringFor_array_negative_vals2([-1, 4, -5, 67, -55, 42]))
## TODO: Print all odd integers from 1 to 255.
def print_odds_1_to_255():
    for i in range(1,256,2):
        print(i)

# print_odds_1_to_255()
## TODO: Iterate through a given array, printing each value.
def print_array_vals(list_param):
    for i in list_param:
        print(i)

# print_array_vals([1,2,3,5,7,9])
## TODO: Analyze an array’s values and print the average
def print_average_of_array(list_param):
    sum = 0
    for i in range(len(list_param)):
        print(i + 1,".", list_param[i])
    #     sum += i
    # print(sum/len(list_param))

# print_average_of_array(['buddy','roy','eric','nick','ryan','jahmil'])
## TODO: Square each value in a given array, returning that same array with changed values
def square_array_vals(list_param):
    for i in range(len(list_param)):
       list_param[i] = list_param[i] * list_param[i]
    return list_param

def square_array_vals2(list_param):
    new_list = []
    for i in list_param:
        print(i)
        new_list.append(i**2)
        print(i)
    return new_list
        

# print(square_array_vals2([1,2,3,4])) #\=> [1,4,9,16]
## TODO: Return the given array, after setting any negative values to zero.
def zero_out_array_negative_vals(arr):
    pass


## TODO: Given an array, move all values forward by one index, dropping the first and leaving a '0' value at the end.
def shift_array_vals_left(list_param):
    for i in range(len(list_param)- 1):
        list_param[i] = list_param[i + 1]
    list_param[-1] = 0
    print(list_param)
    
def shift_array_vals_left(list_param):
    for i in range(len(list_param)):
        if i == len(list_param) - 1:
            list_param[i] = 0
        else:
            list_param[i] = list_param[i + 1]
    print(list_param)

shift_array_vals_left([1,2,3,4,5]) #=> [2,3,4,5,0]