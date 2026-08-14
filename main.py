from config.connection import getConnection

from controllers import supplierController
from controllers.categoryController import CategoryController
from controllers.productController import ProductController
from controllers.supplierController import SupplierController
from controllers.userController import UserController
from models.cart import Cart
from controllers.cartController import CartController
from controllers.orderController import OrderController



""" userController = UserController()
user = userController.register()
user = userController.updateUser()

user= userController.getAllUsers()
user = userController.getUser()
user = userController.deleteUser()
 """


""" categoryController = CategoryController()
categoryController.createCategory()
categoryController.getAllCategories()
categoryController.getCategoryById()
categoryController.updateCategory()
categoryController.deleteCategory() """



""" supplierController = SupplierController()
supplierController.createSupplier()
supplierController.getAllSuppliers()
supplierController.getSupplierById()
supplierController.updateSupplier()
supplierController.deleteSupplier() """


""" productController = ProductController()
productController.createProduct()
productController.updateProduct()
productController.getAllProducts()
productController.getProductById()
productController.getProductByCategory()
productController.getProductBySupplier()
productController.deactivateProduct()
productController.activateProduct()
 """


""" cart = Cart(1)
cartController = CartController()
cartController.addProduct(cart)
cartController.addProduct(cart)
cartController.addProduct(cart)
cartController.addProduct(cart)
cartController.displayCart(cart)
cartController.updateQuantity(cart)
cartController.displayCart(cart)
cartController.removeProduct(cart)
cartController.displayCart(cart) """


userId = 2

cart = Cart(userId)

cartController  = CartController()
orderController  = OrderController()
productController = ProductController()

#orderController.getOrderById()

while True:
    print("----------WELCOME----------------")
    print("1. Add Product")
    print("2. View Cart")
    print("3. Update Cart")
    print("4. Remove Product")
    print("5. Checkout")
    print("6. View Products")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        cartController.addProduct(cart)
    elif choice == "2":
        cartController.displayCart(cart)
    elif choice == "3":
        cartController.updateQuantity(cart)
    elif choice == "4":
        cartController.removeProduct(cart)
    elif choice == "5":
        orderController.checkout(cart)
    elif choice == "6":
        productController.getAllProducts()
    elif choice == "7":
        print("Thank you..")
        break
    else:
        print("Invalid chocie")







