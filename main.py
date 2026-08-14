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


""" userId = 2

cart = Cart(userId)

cartController  = CartController()
orderController  = OrderController()
productController = ProductController() """


""" user1 = 1
user2  = 2 """

""" orderController.getUserOrders(user1)
orderController.getUserOrders(user2) """


#orderController.getAllOrders()
#orderController.getOrderById()





class UserMenu:
    def __init__(self):
        pass

    def userMenu(self):
        userId = input("enter user id")
        try:
            #userId = int(userId)
            #cart = Cart(userId)
            userController = UserController()
            
            user= userController.login()
            userId = int(user.id)
            cart = Cart(userId)

            

            cartController  = CartController()
            orderController  = OrderController()
            productController = ProductController()
        except Exception as err:
            print("Please enter a valid id")

        while True:
            print("----------WELCOME----------------")
            print("1. Add Product")
            print("2. View Cart")
            print("3. Update Cart")
            print("4. Remove Product")
            print("5. Checkout")
            print("6. View Products")
            print("7. Get Order History")
            print("8. Exit")

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
                productController.getAllActiveProducts()
            elif choice =="7":
                orderController.getUserOrders(userId)
            elif choice == "8":
                print("Thank you..")
                break
            else:
                print("Invalid choice")




class AdminMenu:

    def adminMenu(self):
        userId = input("enter user id")
        try:
            userId = int(userId)       
            
            orderController  = OrderController()
            productController = ProductController()
            categoryController = CategoryController()
            supplierController = SupplierController()
        except Exception as err:
            print("Please enter a valid id")

        while True:
            print("----------WELCOME----------------")
            print("1. Get All Suppliers")
            print("2. Get Supplier By Id")
            print("3. Create Supplier")
            print("4. Update Supplier")
            print("5. Delelte Supplier")
            print("6. Get All Categories")
            print("7. Get Category BY id")
            print("8. Add Category")
            print("9. Update Category")
            print("10. Delete Category")
            print("11. Get All products")
            print("12. Get product by id")
            print("13. Create Product")
            print("14. Update Product")
            print("15. Activate Product")
            print("16. Deactivate Product")
            print("17. Exit Admin Panel")

            choice = input("Enter choice: ")

            if choice == "1":
                supplierController.getAllSuppliers()
                
            elif choice == "2":
                supplierController.getSupplierById()
            elif choice == "3":
                supplierController.createSupplier()
                
            elif choice == "4":
                supplierController.updateSupplier()
            elif choice == "5":
                supplierController.deleteSupplier()
            elif choice == "6":
                categoryController.getAllCategories()
            elif choice =="7":
                categoryController.getCategoryById()     
            elif choice == "8":
                categoryController.createCategory()
            elif choice == "9":
                categoryController.updateCategory()
            elif choice =="10":
                categoryController.deleteCategory()    
            elif choice == "11":
                productController.getAllProducts()
                
            elif choice == "12":
                productController.getProductById()
            elif choice == "13":
                productController.createProduct()
            elif choice == "14":
                productController.updateProduct()
            elif choice == "15":
                productController.activateProduct()
            elif choice == "16":
                productController.deactivateProduct()    
            elif choice == "17":
                print("Existing Admin Panel")         
                break          
            
            else:
                print("Invalid choice")







def start():

    while True:
        print("1. Login As Admin")
        print("2. Login As User")
        print("3. Exit")
        choice = input("Enter Choice: ")
       

        if choice == "1":
            a1 = AdminMenu()
            a1.adminMenu()

        elif choice == "2":
            u1 = UserMenu()
            u1.userMenu()
        elif choice == "3":
            break
        else:
            print("Invalid Choice")






start()