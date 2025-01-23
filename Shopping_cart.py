class ShoppingCart:

    def __init__(self):
        self.cart = {}

    def add_item(self, item_name, price, quantity=1):
        if item_name in self.cart:
            self.cart[item_name]["quantity"] += quantity
        else:
            self.cart[item_name] = {"price": price, "quantity": quantity}
        print(f"Added {quantity} x {item_name} to your cart.")

    def remove_item(self, item_name):
        if item_name in self.cart:
            del self.cart[item_name]
            print(f"Removed {item_name} from the cart.")
        else:
            print(f"Item {item_name} not found in the cart.")

    def quantity_update(self, item_name, quantity):
        if item_name in self.cart:
            if quantity > 0:
                self.cart[item_name]["quantity"] = quantity
                print(f"Updated {item_name} quantity to {quantity}.")
            else:
                self.remove_item(item_name)
        else:
            print(f"Item {item_name} not found in the cart.")

    def view_item(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("\nItems in your cart:")
            for item, details in self.cart.items():
                print(f"{item}: Rs.{details['price']} x {details['quantity']}")

    def calculate_total(self):
        return sum(details["price"] * details["quantity"] for details in self.cart.values())
    
    def checkout(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            total = self.calculate_total()
            print("\n--- Checkout ---")
            self.view_item()
            print(f"Total: Rs.{total}")
            print("Thank you for shopping.")
            self.cart.clear()

def main():
    cart = ShoppingCart()

    while True:
        print("\n=== Shopping Cart Menu ===")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Update Quantity")
        print("4. View Items")
        print("5. Checkout")
        print("6. Exit")

        choice = input("Enter Your Choice => ")

        if choice == "1":
            item_name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter quantity: "))
            cart.add_item(item_name, price, quantity)
        elif choice == "2":
            item_name = input("Enter item name: ")
            cart.remove_item(item_name)
        elif choice == "3":
            item_name = input("Enter item name to update: ")
            quantity = int(input("Enter quantity to update: "))
            cart.quantity_update(item_name, quantity)
        elif choice == "4":
            cart.view_item()
        elif choice == "5":
            cart.checkout()
        elif choice == "6":
            print("Exiting! Goodbye.")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()