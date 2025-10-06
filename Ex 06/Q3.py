# Q3) Online Shopping Cart:
# Develop an online shopping cart system with classes for products, 
# customers, shopping carts, orders, and payment processing.

class Product:
    def __init__(self, name, price, product_id):
        self.name = name
        self.price = price
        self.product_id = product_id

    def printData(self):
        print(f"Product {self.product_id}: {self.name} - ${self.price}")


class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id

    def printData(self):
        print(f"Customer {self.customer_id}: {self.name}")


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity=1):
        self.items.append((product, quantity))
        print(f"Added {quantity} x {product.name} to cart.")

    def remove_product(self, product_id):
        for item in self.items:
            if item[0].product_id == product_id:
                self.items.remove(item)
                print(f"Removed {item[0].name} from cart.")
                return
        print("Product not found in cart.")

    def view_cart(self):
        print("\nShopping Cart:")
        if not self.items:
            print("Cart is empty.")
            return
        total = 0
        for product, quantity in self.items:
            print(f"{quantity} x {product.name} - ${product.price * quantity}")
            total += product.price * quantity
        print(f"Total Amount: ${total}")
        return total


class Order:
    order_counter = 1

    def __init__(self, customer, cart):
        self.order_id = Order.order_counter
        Order.order_counter += 1
        self.customer = customer
        self.cart = cart
        self.total_amount = cart.view_cart()

    def print_order(self):
        print(f"\nOrder ID: {self.order_id}")
        self.customer.printData()
        self.cart.view_cart()


class Payment:
    def process_payment(self, order, payment_mode="Credit Card"):
        print(f"\nProcessing {payment_mode} payment for Order {order.order_id}...")
        print(f"Payment of ${order.total_amount} successful. Thank you, {order.customer.name}!")


#Create some products
p1 = Product("Laptop", 1000, 101)
p2 = Product("Headphones", 100, 102)
p3 = Product("Mouse", 50, 103)

#Create customer
c1 = Customer("Suhana", 201)

#Create shopping cart and add products
cart = ShoppingCart()
cart.add_product(p1)
cart.add_product(p2, 2)
cart.add_product(p3)

#View cart
cart.view_cart()

#Create order
order = Order(c1, cart)
order.print_order()

#Make payment
payment = Payment()
payment.process_payment(order)
