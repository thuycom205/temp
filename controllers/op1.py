from time import sleep, time


# def f():
#     sleep(.3)
#
#
# def g():
#     sleep(.5)
#
#
# t = time()
# f()
# print('f took:', time() - t)
#
# t = time()
# g()
# print('g took:', time() - t)

# def f():
#     sleep(.3)
#
#
# def g():
#     sleep(.5)
#
#
# def measure(func):
#     t = time()
#     func()
#     print(func.__name__, 'took:', time() - t)
#
#
# measure(f)
# measure(g)


# from time import sleep, time
#
#
# def f(sleep_time=0.1):
#     sleep(sleep_time)
#
#
# def measure(func, *args, **kwargs):
#     t = time()
#     func(*args, **kwargs)
#     print(func.__name__, 'took:', time() - t)
#
#
# measure(f, sleep_time=0.3)
# measure(f, 0.2)


from time import sleep, time


def f(sleep_time=0.1):
    sleep(sleep_time)


def measure(func):
    def wrapper(*args, **kwargs):
        t = time()
        func(*args, **kwargs)
        print(func.__name__, 'took:', time() - t)

    return wrapper


f = measure(f)  # decoration point
f(0.2)
f(sleep_time=0.3)
print(f.__name__)

from time import sleep, time
from functools import wraps


def measure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = time()
        result = func(*args, **kwargs)
        print(func.__name__, 'took:', time() - t)
        return result

    return wrapper


def max_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 100:
            print(f'Result is too big ({result}). Max allowed is 100.')
        return result

    return wrapper


@measure
@max_result
def cube(n):
    return n ** 3


print(cube(2))
print(cube(5))