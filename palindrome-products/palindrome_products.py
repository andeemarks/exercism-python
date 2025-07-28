from functools import cache
from typing import Callable

product_cache = {}

def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    return select(min_factor, max_factor, max)



def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    return select(min_factor, max_factor, min)
    
def select(min_factor: int, max_factor: int, selector: Callable):
    if (min_factor > max_factor):
        raise ValueError("min must be <= max")

    selected_palindrome_product = None
    selected_palindrome_factors = []

    products = products_between(min_factor, max_factor)
    try:
        selected_palindrome_product = selector(products.keys())
        selected_palindrome_factors = products[selected_palindrome_product]
    except ValueError:
        pass

    return (selected_palindrome_product, selected_palindrome_factors)

@cache
def products_between(min_factor: int, max_factor: int) -> dict:
    palindrome_products = {}
    starting_j_offset = 0
    for i in range(min_factor, max_factor + 1):
        for j in range(min_factor + starting_j_offset, max_factor + 1):
            product = i * j
            product_digits = str(product)
            if (product_digits == product_digits[::-1]):
                factors = [i, j]
                if (palindrome_products.get(product)):
                    palindrome_products[product].append(factors)
                else:
                    palindrome_products[product] = [factors]

        starting_j_offset += 1

    return palindrome_products
