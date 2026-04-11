import time


def logger(func):
    # TODO: реалізувати декоратор
    def wrapper(*args, **kwargs):
        print(f"Function: {func.__name__}")
        print(f"Args: {args} {kwargs}")

        result = func(*args, **kwargs)


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def main():
    print(add(2, 3))
    print(multiply(4, 5))


if __name__ == "__main__":
    main()