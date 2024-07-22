import time
from functools import wraps


def outer_function(message):
    def inner_function():
        print(message)

    return inner_function()


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        original_function(*args, **kwargs)

    return wrapper_function


class DecoratorClass(object):
    def __init__(self, original_function):
        self.function = original_function

    def __call__(self, *args, **kwargs):
        print('call method executed this before {}'.format(self.function.__name__))
        return self.function(*args, **kwargs)


@decorator_function
def display():
    print('display function ran')


# display()


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__, level=logging.INFO))

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'ran with args:{}, and kwargs:{}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in:{} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper


@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({},{})'.format(name, age))


display_info('not amin', 21)
