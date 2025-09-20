class Product:
    inventory = [] 
    product_counter = 0

    def __init__(self,product_id, name, category, quantity, price, supplier):
        self.product_id = product_id
        self.name = name
        self.cathegory = category
        self.quantity = quantity
        self.price = price
        self.supplier = supplier

    @classmethod
    def add_product(cls, name, category, quantity, price, supplier):
        cls.product_counter += 1
        new_product = Product(cls.product_counter, name, category, quantity, price, supplier)
        cls.inventory.append(new_product)
        return "Product added successfully"

    @classmethod
    def update_product(cls,product_id, quantity=None, price=None):
        for product in cls.inventory:
            if product.product_id == product_id:
                if quantity is not None:
                    product.quantity = quantity
                if price is not None:
                    product.price = price
                return "Product information updated successfully"
        return "Product not found"
    
    @classmethod
    def delete_product(cls, product_id):
        for product in cls.inventory:
            if product.product_id == product_id:
                cls.inventory.remove(product)
                return "Product deleted successfully"
        return "Product not found"
    
    @classmethod
    def display_inventory(cls):
        for product in cls.inventory:
            print(f"ID: {product.product_id}, Name: {product.name}, Category: {product.cathegory}, Quantity: {product.quantity}, Price: {product.price}, Supplier: {product.supplier}")

class Order:
    def __init__(self, order_id, product_id, quantity, customer_info):
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.customer_info = customer_info

    def place_order(self):
        for product in Product.inventory:
            if product.product_id == self.product_id:
                if product.quantity >= self.quantity:
                    product.quantity -= self.quantity
                    return "Order placed successfully"
                else:
                    return "Insufficient stock"
        return "Product not found"
    
print(Product.add_product("Smartphone", "Electronics", 30, 500, "Samsung"))
print(Product.add_product("T-shirt", "Clothing", 40, 200, "Levis"))
print(Product.add_product("Blender", "Home Appliances", 20, 150, "Philips"))
print(Product.update_product(1, quantity=45, price=950))
print(Product.delete_product(2))
order1 = Order(order_id=1, product_id=1, quantity=2, customer_info="John Doe")
print(order1.place_order())
print("\nCurrent Inventory: ")
Product.display_inventory()
