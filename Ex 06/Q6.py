# Q6) Inventory Management System:
# Create an inventory management system for a store or warehouse. Implement 
# classes for products, suppliers, inventory, orders (purchases, sales), 
# and stock management.

class Product:
    def __init__(self, name, product_id, price):
        self.name = name
        self.product_id = product_id
        self.price = price

    def printData(self):
        print(f"Product {self.product_id}: {self.name}, Price: ${self.price}")


class Supplier:
    def __init__(self, name, supplier_id):
        self.name = name
        self.supplier_id = supplier_id

    def printData(self):
        print(f"Supplier {self.supplier_id}: {self.name}")


class Inventory:
    def __init__(self):
        self.stock = {}  # product_id: quantity

    def add_stock(self, product, quantity):
        if product.product_id in self.stock:
            self.stock[product.product_id] += quantity
        else:
            self.stock[product.product_id] = quantity
        print(f"Added {quantity} units of {product.name}. Total stock: {self.stock[product.product_id]}")

    def remove_stock(self, product, quantity):
        if product.product_id in self.stock and self.stock[product.product_id] >= quantity:
            self.stock[product.product_id] -= quantity
            print(f"Removed {quantity} units of {product.name}. Remaining stock: {self.stock[product.product_id]}")
        else:
            print(f"Insufficient stock for {product.name} or product not found.")

    def show_stock(self, products):
        print("\nCurrent Inventory:")
        for product in products:
            qty = self.stock.get(product.product_id, 0)
            print(f"{product.name} (ID: {product.product_id}) - Stock: {qty}")


class Order:
    order_counter = 1

    def __init__(self, product, quantity, order_type):  # order_type: "Purchase" or "Sale"
        self.order_id = Order.order_counter
        Order.order_counter += 1
        self.product = product
        self.quantity = quantity
        self.order_type = order_type

    def printData(self):
        print(f"Order {self.order_id}: {self.order_type} {self.quantity} units of {self.product.name}")


class Store:
    def __init__(self):
        self.products = []
        self.suppliers = []
        self.inventory = Inventory()
        self.orders = []

    def add_product(self, product):
        self.products.append(product)

    def add_supplier(self, supplier):
        self.suppliers.append(supplier)

    def make_order(self, order):
        self.orders.append(order)
        if order.order_type == "Purchase":
            self.inventory.add_stock(order.product, order.quantity)
        elif order.order_type == "Sale":
            self.inventory.remove_stock(order.product, order.quantity)
        order.printData()

    def show_inventory(self):
        self.inventory.show_stock(self.products)


store = Store()

#Add suppliers
s1 = Supplier("Suhana Suppliers", 301)
s2 = Supplier("Aman Traders", 302)
store.add_supplier(s1)
store.add_supplier(s2)

#Add products
p1 = Product("IPad", 101, 1000)
p2 = Product("Tablet", 102, 25)
p3 = Product("Notepad", 103, 50)
store.add_product(p1)
store.add_product(p2)
store.add_product(p3)

#Make purchase orders
o1 = Order(p1, 10, "Purchase")
o2 = Order(p2, 50, "Purchase")
o3 = Order(p3, 30, "Purchase")
store.make_order(o1)
store.make_order(o2)
store.make_order(o3)

#Make sale orders
o4 = Order(p2, 5, "Sale")
o5 = Order(p1, 2, "Sale")
store.make_order(o4)
store.make_order(o5)

#Show inventory
store.show_inventory()
