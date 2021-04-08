import time

def timer(func):

    def wrapper(*args,**kwargs):
        start = time.perf_counter_ns()
        func(*args,**kwargs)
        end = time.perf_counter_ns()
        print(f'time to run: {end-start} nanoseconds')

    return wrapper

@timer
def say_hello(name):
    print('wassup' + name)

#timer(say_hello)('tim')

say_hello('john')