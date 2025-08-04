""" 4. Mix Arguments
Write a function order(item, quantity=1, *extras, **details) that:

Prints the item & quantity.

Prints any extra toppings (from *extras).

Prints other details like address, phone (from **details).
"""

def order(item, quantity=1, *extras, **details):
    print(f"item: {item}")
    print(f"quantity: {quantity}")

    if extras:
        print("Extras")
        for e in extras:
            print(f"{e}")

    if details:
        print("other details")
        for key, value in details.items():
            print(f"{key}: {value}")


order("Pizza",
      2,
      "cheese Burst",
      "Extra olives",
      address = 'Achalapur',
       phone = 8565475869)