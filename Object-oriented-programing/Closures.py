def outer_function(msg):
    message = msg

    def inner_function():
        print(message)

    return inner_function


hi_function = outer_function('hi')
hello_function = outer_function('hello')

# hi_function()
# hello_function()

import logging

logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):
    def log_func(*args):
        logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))

    return log_func


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3, 3)
sub_logger(4, 5)
