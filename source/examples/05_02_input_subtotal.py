item_name = input("商品名を入力してください: ")
price = int(input("1つの値段を入力してください: "))
quantity = int(input("個数を入力してください: "))

subtotal = price * quantity

print(f"{item_name} の小計は {subtotal} 円です")
