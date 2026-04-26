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


def member_label(is_member):
    if is_member:
        return "会員"

    return "一般"


def main():
    print("おはなしレジアプリへようこそ！")

    customer_name = input("お客さんの名前を入力してください: ")
    item_name = input("商品名を入力してください: ")
    price = int(input("1つの値段（円）を入力してください: "))
    quantity = int(input("個数を入力してください: "))
    member_answer = input("会員ですか？ (y/n): ").strip().lower()

    is_member = member_answer == "y"

    subtotal, member_discount, bulk_discount, total = calculate_total(
        price, quantity, is_member
    )

    print()
    print("--- お会計 ---")
    print(f"{customer_name}さん、ありがとうございます。")
    print(f"商品: {item_name}")
    print(f"区分: {member_label(is_member)}")
    print(f"小計: {subtotal}円")
    print(f"会員割引: -{member_discount}円")
    print(f"まとめ買い割引: -{bulk_discount}円")
    print(f"合計: {total}円")
    print("またおはなしの世界へどうぞ！")


if __name__ == "__main__":
    main()
