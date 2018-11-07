pending_orders = []
delivered_orders = [1, 2, 3, 4, 5, 6]

def check_order_status(order_id):
    if order_id in delivered_orders:
        return True
    return False

def check_order_pending(order_id):
    if order_id in pending_orders:
        return True
    return False

def check_integer(order_id):
    if isinstance(order_id, int):
        return True
    return False

def check_exist_both(order_id):
    if order_id in delivered_orders and order_id in pending_orders:
        return True
    return False

def check_adding_pending(order_id):
    if order_id in pending_orders:
        return True
    return False