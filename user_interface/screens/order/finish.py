import tkinter as tk

from user_interface.screens.clear_window import clear_window


def finish_order(window, user):
    clear_window(window)

    with open('./db/orders/current_order.txt', 'a') as order_file:
        order_file.write(f'Waiter : {user}')

