subtotal = 2400
member_answer = input("会員ですか？ (y/n): ").strip().lower()

if member_answer == "y":
    discount = int(subtotal * 0.1)
else:
    discount = 0

total = subtotal - discount

print(f"値引き額は {discount} 円です")
print(f"お会計は {total} 円です")
