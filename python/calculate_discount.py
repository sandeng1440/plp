def calculate_discount(price: float, discount_percent: int) -> float:
    if discount_percent >= 20:
        price = price - (price * discount_percent / 100)
    return price


price = int(input("Enter the price: "))
discount_percent = int(input("Enter the discount percentage: "))

print(f"Discounted Price: { calculate_discount(price, discount_percent)}")
