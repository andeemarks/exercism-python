from functools import reduce

def largest_product(series, length):
    if (len(series) < length):
        raise ValueError("span must not exceed string length")
    
    if (length < 0):
        raise ValueError("span must not be negative")
    
    try:
        int(series)
    except ValueError:
        raise ValueError("digits input must only contain digits")

    return max(find_products_for(series, length))

def find_products_for(series: str, length: int) -> list[int]:
    return [find_product_for(series[i:i+length]) for i in range(len(series) - length + 1)]

def find_product_for(span: str) -> int:
    return reduce(lambda x, y: int(x) * int(y), span)
