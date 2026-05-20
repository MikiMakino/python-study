def calculate_total(price, quantity, is_member):
    subtotal = price * quantity

    if is_member:
        member_discount = int(subtotal * 0.1)
    else:
        member_discount = 0

    if quantity >= 3:
        bulk_discount = 100
    else:
        bulk_discount = 0

    total = subtotal - member_discount - bulk_discount
    return subtotal, member_discount, bulk_discount, total


print(calculate_total(1200, 3, True))
