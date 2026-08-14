from config.connection import getConnection
from mappers.orderMapper import mapRowToOrder


class OrderDao:
    def createOrder(self, order, conn):

        query = "INSERT INTO orders(user_id) VALUES(%s)"
        cursor = conn.cursor()
        cursor.execute(query, (order.userId,))

        order.id = cursor.lastrowid
        cursor.close()
        return order

    def getOrderById(self, orderId):

        query = "SELECT id, user_id, created_at, updated_at FROM orders WHERE id=%s"
        conn = getConnection()
        cursor = conn.cursor(dictionary=True)
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return mapRowToOrder(row)

    def getOrderByUser(self, userId):
        query = "SELECT id, user_id, created_at, updated_at FROM orders where user_id = %s ORDER BY created_at DESC"
        conn = getConnection()
        cursor = conn.cursor(dictionary=True)
        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        return [
            mapRowToOrder(row)
            for row in rows
        ]