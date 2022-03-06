def func_counter(func):
    def wrapper(param):
        wrapper.counter += 1
        return func(param)
    wrapper.counter = 0
    return wrapper
