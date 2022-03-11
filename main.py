from sort import sort_list
import timeit
import tracker

def main():
    #test_p1()
    #test_p3()
    test_p5()

def test_p1():
    print("----- Problem 1 -----")
    print(sort_list([1, 3, 2, 7]))
    print(sort_list([3, 2, 4, 89]))
    print(sort_list([]))
    print(sort_list([1]))
    print(sort_list(['A', 'E', 'B', 'G', 'H']))
    print(sort_list(['a', 4, 'c', 2]))
    print(sort_list([5, 4, 3, 2, 1, 0]))
    print("---------------------")

def test_p3():
    p3_sort_list()

@timeit.calculate_time
def p3_sort_list():
    lst = []
    for j in range(5000, 0, -1):
        lst.append(j)
    sort_list(lst)

def test_p5():
    print(hello.counter)
    for i in range(5):
        hello(i)
        print(hello.counter)

@tracker.func_counter
def hello(name):
    print(f"Hello {name}!")

if __name__ == '__main__':
    main()
