class Product:
    def __init__(self, categoryId, supplierId, name, unitPrice, stock = 1,isActive=True, id=None):
        self.id = id
        self.categoryId = categoryId
        self.supplierId = supplierId
        self.name = name
        self.unitPrice = unitPrice
        self.isActive = isActive
        