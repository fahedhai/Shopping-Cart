"""
CSC1401 Assessment 3 - Shopping Cart Simulation

A command-line shopping cart program: users browse a catalogue of 40
products, add items to their cart (choosing membership status, quantity,
and shipping method), then view an itemized summary, total cost, and a
version of the cart sorted and merged by product code.

Team ID: 37
Authors: Xavier Jackson, Fahed Haidar
"""

product_list = ['Salad Server Set', 'Party Serviette Holder', 'Tea Set', 'Mixing Bowl Set', 'Knife Block Set', 'Coffee Capsule Holder',
                'Plastic Sensor Soap Pump', 'Storage Bucket', 'Oven Glove', 'Apron', 'Biscuit Barrel', 'Chopping Board', 'Carioca Cups',
                'Soup Bowls', 'Elevate Wood Turner', 'Pasta Machine', 'Teapot', 'Cake Pop Scoop', 'Cookbook Stand', 'Chocolate Station',
                'Coffee Maker', 'Pepper Mill', 'Salt Mill', 'Glass Storage Jar', 'Measuring jug', 'Kitchen Scale', 'Tenderiser',
                'Pizza Docker', 'Knife Sharpener', 'Steel Cork Opener', 'Steel Garlic Press', 'Steel Can Opener',
                'Stainless Steel Crank Flour Sifter', 'Mineral Stone Mortar and Pestle', 'Citrus Cather', 'Cherry & Olive Pitter',
                'Multi Grater-Detachable', 'Stainless Steel Colander', 'Steel Pizza Pan', 'Pop Container']

price_list = [18.70, 11.95, 39.95, 49.95, 99.95, 29.95, 79.95, 24.95, 9.95, 29.95,
              39.95, 12.95, 54.95, 43.00, 19.95, 144.95, 29.95, 9.95, 29.95, 34.95,
              29.00, 84.94, 84.95, 4.95, 19.95, 39.95, 34.95, 19.95, 79.95, 36.95,
              34.95, 36.95, 33.95, 74.95, 19.95, 27.95, 26.95, 44.95, 12.95, 22.95]

shopping_record = []


def show_catalogue():
    print("Catalogue\n")
    print(f"{'Code':4}  {'Product':35} {'Price $':>8}     {'Code':4}  {'Product':35} {'Price $':>8}")
    print(f"{'----':4}  {'-'*35}  {'-'*8}    {'----':4}  {'-'*35}  {'-'*8}")
    for i in range(0, 40, 2):
        left = f"{i:<4}  {product_list[i]:35}  {price_list[i]:<8.2f}"
        if i + 1 < len(product_list):
            right = f"{i+1:<4}  {product_list[i+1]:35}  {price_list[i+1]:<9.2f}"
        print(left + "    " + right)


def is_valid_code(code):
    if not code.isdigit():
        print("Error: Product code must be an integer.")
        return False

    code = int(code)

    if code < 0 or code > 39:
        print("Error: Product code must be between 0 and 39.")
        return False

    return True


def is_valid_quantity(quantity):
    if not quantity.isdigit():
        print("Error: Quantity must be an integer.")
        return False

    quantity = int(quantity)

    if quantity <= 0 or quantity > 29:
        print("Error: Quantity must be between 1 and 29.")
        return False

    return True


def add_record():
    membership_status = input("Are you a member? (Yes/No/End): ")

    if membership_status.lower() == "end":
        return "End"
    if membership_status.lower() not in ("yes", "no"):
        print("Error: Membership status must be either Yes, No, or End")
        return

    code = input("Please enter a product code (0-39): ")
    if not is_valid_code(code):
        return

    code_int = int(code)
    product_name = product_list[code_int]
    price = price_list[code_int]

    quantity_input = input("Please enter desired quantity (1-29): ")
    if not is_valid_quantity(quantity_input):
        return

    quantity_int = int(quantity_input)

    shipping_method = input("Please enter desired shipping method (Delivery/Pick-up): ")
    if shipping_method not in ("Delivery", "Pick-up"):
        print("Error: Shipping method must be 'Delivery' or 'Pick-up' (case sensitive)")
        return

    if shipping_method == "Delivery":
        shipping_fee = round(2 + (quantity_int - 1) * 1.6, 2)
    else:
        shipping_fee = 0

    subtotal = (price * quantity_int) + shipping_fee
    if membership_status.lower() == "yes":
        membership_status = ("Yes")
        total_record_cost = round(subtotal * 0.9, 2)
    else:
        membership_status = ("No")
        total_record_cost = round(subtotal, 2)

    record = (f"{membership_status}; {code_int}; {product_name}; {price}; "
              f"{quantity_int}; {shipping_method}; {shipping_fee}; {total_record_cost}")

    shopping_record.append(record)
    print("Record added")


def total_cost():
    if not shopping_record:
        print("You have not selected any items to buy")
        return
    total = 0.0
    for record in shopping_record:
        splits = record.split("; ")
        total += float(splits[7])
    print(f"\nThe total cost is ${total:.2f}")


def show_record():
    if not shopping_record:
        print("\nYou have not selected any items to buy,")
        return
    print(f"\n{'Membership':11} {'Code':5} {'Product':35} {'Price $':9}"
          f"{'Quantity':9} {'Shipping method':16} {'Shipping fee $':15} {'Cost $'}")
    print(f"{'-'*10:12}{'-'*4:6}{'-'*35:36}{'-'*7:9}"
          f"{'-'*8:10}{'-'*15:17}{'-'*14:16}{'-'*6}")
    for record in shopping_record:
        splits = record.split("; ")
        membership = splits[0]
        code = splits[1]
        product = splits[2]
        price = splits[3]
        quantity = splits[4]
        shipping_method = splits[5]
        shipping_fee = splits[6]
        cost = splits[7]
        print(f"{membership:11} {code:5} {product:35} {price:9}"
              f"{quantity:9} {shipping_method:16} {shipping_fee:15} {cost}")
    total_cost()


def sort_records():
    if not shopping_record:
        print("There are no records to show")
        return
    sorted_records = sorted(shopping_record, key=lambda r: int(r.split("; ")[1]))
    merged = {}
    for record in sorted_records:
        splits = record.split("; ")
        code = int(splits[1])
        product = splits[2]
        price = float(splits[3])
        quantity = int(splits[4])
        cost = float(splits[7])
        if code in merged:
            merged[code][2] += quantity
            merged[code][3] = round(merged[code][3] + cost, 2)
        else:
            merged[code] = [product, price, quantity, cost]
    print(f"\n{'Code':6}{'Product':36}{'Price $':10}{'Quantity':10}{'Cost $'}")
    print(f"{'-'*4:6}{'-'*35:36}{'-'*7:10}{'-'*8:10}{'-'*6}")

    for code, (product_name, unit_price, total_qty, total_cost_val) in merged.items():
        print(f"{code:<6}{product_name:36}{unit_price:<10.2f}"
              f"{total_qty:<10}{total_cost_val:.2f}")


def main():
    shopping_record.clear()
    show_catalogue()

    while True:
        result = add_record()
        if result == "End":
            break

    show_record()
    sort_records()


if __name__ == "__main__":
    main()
