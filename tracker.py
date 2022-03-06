def func_counter(func):
    def wrapper(name):
        wrapper.counter += 1
        return func(name)
    wrapper.counter = 0
    return wrapper
