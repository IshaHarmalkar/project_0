class OrderDetail:
    def __init__(self, orderId, productId,  unitPriceAtPurchase, qty=1):
        self.orderId = orderId
        self.productId = productId
        self.qty = qty
        self.unitPriceAtPurchase = unitPriceAtPurchase