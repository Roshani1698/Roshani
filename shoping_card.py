# Shopping Cart

class Product:
    def __init__(self, name, price):
        self.name=name
        self.price=price

class cart:
    def __init__(self):
        self.products=[]

    def add_product(self,product):
        self.products.append(product)

    def total_price(self):
        return sum(p.price for p in self.products)

    def display(self):
        print("cart items")
        for p in self.products:
            print(p.name, p.price)
            print(f"Total price: {self.total_price()}")


p1 = Product("Laptop",70000)
p2 = Product("Headphone", 2000)
p3 = Product("TV", 75000)


cart = cart()

cart.add_product(p1)
cart.add_product(p2)
cart.add_product(p3)

cart.display()

