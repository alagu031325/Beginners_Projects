# Implementation of Binary Search Algorithm


# Binary search is faster than naive search

# Naive search
def naive_search(search_list, target):
    for i in range(len(search_list)):
        if search_list[i] == target:
            return i
    return -1


# Binary search - uses divide and conquer algorithm
def binary_search(search_list, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(search_list) - 1

    # Integer division to return the result as an integer
    midpoint = (low + high) // 2

    if search_list[midpoint] == target:
        return midpoint
    elif target < search_list[midpoint]:
        return binary_search(search_list, target, low, midpoint - 1)
    else:
        # target > search_list[midpoint]
        return binary_search(search_list, target, midpoint + 1, high)

    # Condition to check if the target is not present in the list
    return -1


if __name__ == '__main__':
    input_string = input("Enter a list of values (comma-separated): ")
    input_list = input_string.split(",")

    # list comprehension is used to convert the values to integers
    input_list = [int(value) for value in input_list]

    length = len(input_list)

    search_integer = int(input("Enter a number to be searched from the list: "))

    # start = time.time()
    # print(naive_search(input_list, search_integer))
    # end = time.time()
    # print("Naive search time: ", (end - start) / length, " seconds")

    print("The position at which the target found is ", binary_search(input_list, search_integer))
