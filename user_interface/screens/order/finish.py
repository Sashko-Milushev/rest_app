import tkinter as tk


def finish_order(window, user, render):

    with open('./db/orders/current_order.txt', 'a') as order_file:
        order_file.write(f'Waiter : {user}')

    with open('./db/orders/current_order.txt', 'r') as order_file:
        for line in order_file:
            print(line)
    render(window)


