import time

def calculate_time(func):
    def wrapper():
        start = time.time()
        func()
        total = time.time() - start
        print(f"Total time {total}")
    return wrapper
