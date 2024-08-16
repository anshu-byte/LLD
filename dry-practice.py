# Don't Repeat Yourself (DRY)


# Example 1
# Wrong way
def calculate_tax_food(price):
    tax_rate = 0.08
    return price * tax_rate


def calculate_tax_clothes(price):
    tax_rate = 0.05
    return price * tax_rate


def calculate_tax_shoes(price):
    tax_rate = 0.02
    return price * tax_rate


# Right way


def calculate_tax(price, tax_rate):
    return price * tax_rate


# Example 2

# Using Decorators for cross cutting concerns


def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@logger
def add(a, b):
    return a + b


@logger
def sub(a, b):
    return a - b


@logger
def mul(a, b):
    return a * b
