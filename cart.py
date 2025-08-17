import json

def get_cart_from_user():
    items = []
    print("لیست خرید را وارد کنید (برای پایان، نام کالا را خالی بگذارید).")
    while True:
        name = input("نام کالا: ").strip()
        if name == "":
            break
        try:
            quantity = int(input("تعداد: "))
            price = int(input("قیمت واحد: "))
        except ValueError:
            print(" عدد معتبر وارد کنید.")
            continue

        items.append({"name": name, "quantity": quantity, "price": price})
    return {"items": items}

def save_cart(cart, filename="cart.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(cart, f, ensure_ascii=False, indent=4)

def load_cart(filename="cart.json"):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def calc_total(cart):
    return sum(item["quantity"] * item["price"] for item in cart["items"])

def print_cart(cart):
    print("\nلیست خرید:")
    for item in cart["items"]:
        print(f"- {item['name']} ({item['quantity']} × {item['price']} تومان)")
    print(f"\nجمع کل: {calc_total(cart):,} تومان")

def main():
    cart = get_cart_from_user()
    save_cart(cart)
    data = load_cart()
    print_cart(data)

if __name__ == "__main__":
    main()
