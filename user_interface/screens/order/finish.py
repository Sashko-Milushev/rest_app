import tkinter as tk

from user_interface.screens.clear_window import clear_window


def finish_order(window):
    clear_window(window)

    with open('./db/orders/current_order.txt', 'r+') as order_file:
        for order_line in order_file:
            print(order_line)
