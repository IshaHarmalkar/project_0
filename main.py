from config.connection import getConnection

from controllers.categoryController import CategoryController
from controllers.supplierController import SupplierController
from controllers.userController import UserController



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



supplierController = SupplierController()
supplierController.createSupplier()
supplierController.getAllSuppliers()
supplierController.getSupplierById()
supplierController.updateSupplier()
supplierController.deleteSupplier()
