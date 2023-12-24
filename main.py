'''
Написать декоратор который будет сохранять(кешировать) результат выполнения любой ф-ции,
то есть, в первый раз ф-ция с одними и теми же параметрами будет запускаться
а во все остальные разы с теми же параметрами результат будет возвращаться из кеша.
'''


def cache_result(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))

        if key in cache:
            print('Результат из кэша')
            return cache[key]

        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return wrapper


@cache_result
def expensive_function(n):
    print("Записан в кэш")
    result = n * 2
    return result


print(expensive_function(5))
print(expensive_function(5))
print(expensive_function(4))
print(expensive_function(3))
print(expensive_function(5))

