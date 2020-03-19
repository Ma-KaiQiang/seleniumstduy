# coding:utf-8
# def debug(func):
#     def wrapper():
#         print ("[DEBUG]: enter {}()".format(func.__name__))
#         return func()
#     return wrapper
#
# @debug
# def say_hello():
#     print ("hello!")
#
#
#
# say_hello()

# def debug(func):
#     def wrapper(*args, **kwargs):
#         print("[DEBUG]: enter {}()".format(func.__name__))
#         return func(*args,**kwargs)
#
#     return wrapper
#
#
# # @debug
# def say_hello(something):
#     print("hello {}".format(something))
#
#
# say_hello=debug(say_hello)  # 添加功能并保持原函数名不变
# say_hello('123')


def logging(level):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print("[{level}]: enter function {func}()".format(
                level=level,
                func=func.__name__))
            return func(*args, **kwargs)

        return inner_wrapper

    return wrapper


@logging(level='INFO')
def say(something):
    print("say {}!".format(something))

say = logging(level='DEBUG')(say('hi'))
# say()
