
CURRENT_ORDER_PATH = 'db/orders/current_order.txt'

def order_append(order, username, func, window):
    with open(CURRENT_ORDER_PATH, 'a') as file:
        file.write(f'{username}: {order}\n')
        func(window)


def clear_current_order():
    open(CURRENT_ORDER_PATH, 'w').close()
