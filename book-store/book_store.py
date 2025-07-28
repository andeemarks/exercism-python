from collections import Counter

book_price = 800

def total(basket):
    distribution = Counter(basket)
    unique_books = len(distribution)

    discounts = {0: 0, 1: 0, 2: 5, 3: 10, 4: 20, 5: 25}
    
    price = 0
    price = apply_discount(unique_books, discounts[unique_books])
    
    print(f"current price: {price}")
    number_of_books_purchased = len(basket)
    if (number_of_books_purchased > unique_books):

        print(f"overflow of {number_of_books_purchased - unique_books} books")
        price += (number_of_books_purchased - unique_books) * book_price

    print(f"final price: {price}")

    return price

def apply_discount(quantity: int, discount: int) -> int:
    print(f"applying discount of {discount} to {quantity} books")
    return book_price * quantity - ((book_price * quantity) * discount / 100)