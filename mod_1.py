


def small_val(*args):
    result = args[0]
    for num in args:
        if num < result:
            result = num
    return result

