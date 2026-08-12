from config.connection import getConnection

from controllers.userController import UserController


conn = getConnection()

controller = UserController()
#u1 = controller.register()
#controller.updateUser()

controller.getAllUsers()
controller.getUser()
#controller.deleteUser()




