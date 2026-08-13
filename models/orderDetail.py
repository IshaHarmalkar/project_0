class OrderDetail:
    def __init__(self,  productId,  unitPriceAtPurchase, qty=1, orderId=None):
        self.orderId = orderId
        self.productId = productId
        self.qty = qty
        self.unitPriceAtPurchase = unitPriceAtPurchase