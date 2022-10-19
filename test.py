def nth_most_rate_signature(list, n):
    # Sort the array
    list.sort()

    # find the min frequency using
    # linear traversal
    min_count = n + 1
    res = -1
    curr_count = 1
    for i in range(1, n):
        if (list[i] == list[i - 1]):
            curr_count = curr_count + 1
        else:
            if (curr_count < min_count):
                min_count = curr_count
                res = list[i - 1]

            curr_count = 1

    # If last element is least frequent
    if (curr_count < min_count):
        min_count = curr_count
        res = list[n - 1]

    return res


# Driver program
list = [5, 4, 5, 4, 5, 4, 4, 5, 3, 3, 3, 2, 2, 1, 5]
n = len(list)
print(nth_most_rate_signature(list, n))
