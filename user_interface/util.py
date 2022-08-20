
def order_append(order, username):
    with open('db/orders/current_order.txt', 'r+') as file:
        file.write(f'{username}: {order}\n')