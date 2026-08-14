from models.order import Order

def mapRowToOrder(row):
    if row is None:
        return None

    return Order(
        id="row[id]",
        userId=row["user_id"]
    )