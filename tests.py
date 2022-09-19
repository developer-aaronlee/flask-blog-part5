from functools import wraps
import time


def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__, " was called")
        return func(*args, **kwargs)

    return with_logging


@logged
def example(x):
    """does some math"""
    return x + x


print(example.__name__)
print(example.__doc__)


def slow_down(func):
    @wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)

    return wrapper_slow_down


@slow_down
def count_down(from_num):
    if from_num < 1:
        print("Liftoff!")
    else:
        print(from_num)
        count_down(from_num - 1)


count_down(3)
