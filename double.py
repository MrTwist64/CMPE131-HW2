def doubler(func):
    def wrapper():
        func()
        func()
        return
    return wrapper
