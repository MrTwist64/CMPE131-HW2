def sort_list(lst):
    if not lst:
        return lst
    n = len(lst)
    i = 0
    while i < n:
        j = i
        while j < n - i - 1:
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
            j += 1
        i += 1
    return lst