import time


def logger(func):
    # TODO: реалізувати декоратор
    def wrapper(*args, **kwargs):
        print(f"Function: {func.__name__}")
        start = time.perf_counter()
        result = func(*args)
        print(f"Time: {(start) * 1000:.6f} ms")

def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def main():
    print(add(2, 3))
    print(multiply(4, 5))


if __name__ == "__main__":
    main()