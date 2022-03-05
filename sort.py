def sort_list(lst):
    # check if list is empty
    # return list if true
    if not lst:
        return lst
    # check if list is all same type
    # return unsorted list if not true
    lstType = type(lst[0])
    for x in lst:
        if lstType != type(x):
            return lst
    # perform BubbleSort
    n = len(lst)
    i = 0
    while i < n:
        j = 0
        while j < n - i - 1:
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
            j += 1
        i += 1
    return lst
