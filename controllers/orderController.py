from services.orderService import OrderService

class OrderController:
    def __init__(self):
        self.orderService = OrderService()

    def checkout(self, cart):
        print("---------CheckOut--------")

        if cart.isEmpty():
            print("Car is empty")
            return

        total = 0

        for item in cart.items:
            subtotal  = (item.unitPriceAtPurchase * item.qty)

            total += subtotal

            print(f"Product Id: {item.productId} |" f"Qty: {item.qty}"f"Price: {item.unitPriceAtPurchase} |"f"Subtotal: {subtotal}")

            print("-------------------------------")
            print("Total: ", total)

            confirm = input("Confirm order? (Y/N): ")

            if confirm.lower() != "y":
                print("Checkput cancelled.")
                return

            try:
                order = self.orderService.checkOut(cart)
                print("Order placed successfully")
                print("Order ID: ", order.id)
                print("Total: ", total)

            except ValueError as err:
                print("Checkout failed: ", err)

            except Exception as err:
                print("Unexcepted error durring checkout: ", err)