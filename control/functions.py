def sum_all_nunmbers(*args):
    total = 0
    for num in args:
        total += num
    return total


# print(sum_all_nunmbers(1, 2, 3, 4))


def show_user_info(**kwargs):
    return kwargs


print(show_user_info(name='amin', age=20, money=0))

