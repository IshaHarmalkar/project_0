from config.connection import getConnection

from controllers import supplierController
from controllers.categoryController import CategoryController
from controllers.productController import ProductController
from controllers.supplierController import SupplierController
from controllers.userController import UserController
from models.cart import Cart
from controllers.cartController import CartController



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


cart = Cart(1)
cartController = CartController()
cartController.addProduct(cart)
cartController.addProduct(cart)
cartController.addProduct(cart)
cartController.addProduct(cart)
cartController.displayCart(cart)
cartController.updateQuantity(cart)
cartController.displayCart(cart)
cartController.removeProduct(cart)
cartController.displayCart(cart)





