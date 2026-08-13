from services.productService import ProductService
from models.product import Product


class ProductController:

    def __init__(self):
        self.productService = ProductService()


    def printProduct(self, product: Product):
        print(f"ID: {product.id}")
        print(f"Category: {product.categoryId}")
        print(f"Supplieer: {product.supplierId}")
        print(f"Name: {product.name}")
        print(f"Unit Price: {product.unitPrice}")
        print(f"Stock: {product.stock}")
        print(f"isActive: {product.isActive}")

    def createProduct(self):
        print("---------Create Product --------")

        categoryId = input("Category Id: ")
        supplierId = input("Supplier Id: ")
        name = input("Product Name: ")
        unitPrice = input("Unit Price: ")
        stock = input("Stock: ")
        isActive = input("Keep Product as Active, (Y/N): ")


        try:
            categoryId = int(categoryId)
            supplierId = int(supplierId)
            unitPrice = float(unitPrice)
            stock = int(stock)
            isActive = True if isActive.lower() == "y" else False

            product = Product(
                categoryId=categoryId,
                supplierId=supplierId,
                name=name,
                unitPrice=unitPrice,
                stock=stock,
                isActive=isActive
            )

            product = self.productService.createProduct(product)
            self.printProduct(product)
            return product

        except ValueError as err:
            print("Could not create product: ", err)

        return None


    def getProductById(self):
        productId = input("Enter product Id: ")

        try:
            productId = int(productId)
            product = self.productService.getProduct(productId)

            print("-------Product--------")
            self.printProduct(product)

            return product
        except ValueError as err:
            print("Failed to get Product: ", err)

        return None


    def getAllProducts(self):

        try:
            products = self.productService.getAllProducts()

            if not products:
                print("No products found")
                return []

            print("-------Products------------")
            for p in products:
                self.printProduct(p)
                print("-------------------------------")

            return products

        except ValueError as err:
            print("Failed to get products: ", err)

        return []

    def updateProduct(self):
        print("----------Update Product------------")
        productId  = input("Product Id: ")
        categoryId = input("Category Id: ")
        supplierId = input("Supplier Id: ")
        name = input("Product name: ")
        unitPrice = input("Unit price: ")
        stock = input("Stocck: ")
        isActive = input("Activate? yes or no: ")


        try:
            productId = int(productId)
            categoryId = int(categoryId)
            supplierId = int(supplierId)
            unitPrice = float(unitPrice)
            stock = int(stock)
            isActive = isActive.lower() == "y"

            product = Product(
                id=productId,
                categoryId=categoryId,
                supplierId=supplierId,
                name=name,
                unitPrice=unitPrice,
                stock=stock,
                isActive=isActive
            )

            updated = self.productService.updateProduct(product)

            if updated:
                print("Product updated successfully")
                self.printProduct(product)
            else:
                print("Product was not updated")

            return updated
        except ValueError as err:
            print("Failed to update product: ", err)

        return False

    def getProductByCategory(self):

        categoryId = input("Enter ccategory Id: ")
        try:
            categoryId = int(categoryId)
            products = self.productService.getProductsByCategory(categoryId)

            if not products:
                print("No products found for this category.")
                return []

            print("-------Products----------")

            for p in products:
                self.printProduct(p)
                print("--------------------")

            return products

        except ValueError as err:
            print("Failed to get products by category: ", err)

        return []

    def getProductBySupplier(self):
    
        supplierId = input("Enter supplier Id: ")
        try:
            supplierId = int(supplierId)
            products = self.productService.getProductsBySupplier(supplierId)

            if not products:
                print("No products found for this supplier.")
                return []

            print("-------Products----------")

            for p in products:
                self.printProduct(p)
                print("--------------------")

            return products

        except ValueError as err:
            print("Failed to get productst by supplier: ", err)

        return []
    


    def deleteProduct(self):
        pass

    def deactivateProduct(self):
        print("--------Deactivate Product --------")
        productId = input("Product Id: ")
        try:
            productId = int(productId)
            confirm = input("Are you sure you want to deactivate this product? (Y/ N): ")

            if confirm.lower() != "y":
                print("Deactivation Cancelled")
                return False

            deactivated = self.productService.deactivateProduct(productId)


            if deactivated:
                print("Product Deactived successfully")

            else:
                print("Product was not deactivated")

            return deactivated

        except ValueError as err:
            print("Failed to deactivate: ", err)

        return False


    def activateProduct(self):
        print("--------Activate Product --------")
        productId = input("Product Id: ")
        try:
            productId = int(productId)

            
            activated = self.productService.activateProduct(productId)


            if activated:
                print("Product Actived successfully")

            else:
                print("Product was not Activated")

            return activated

        except ValueError as err:
            print("Failed to Activate: ", err)

        return False



