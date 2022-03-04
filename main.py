from sort import sort_list

def main():
    test_p1()

def test_p1():
    print("----- Problem 1 -----")
    print(sort_list([1, 3, 2, 7]))
    print(sort_list([3, 2, 4, 89]))
    print(sort_list([]))
    print(sort_list([1]))
    print(sort_list(['a', 'd', 'c', 'b']))
    print("---------------------")

if __name__ == '__main__':
    main()