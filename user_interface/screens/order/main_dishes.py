import json
import tkinter as tk

from user_interface.auth_service import get_current_user
from user_interface.util import order_append


def render_main_dishes(window):
    current_user = get_current_user()
    current_username = current_user['username']

    row = 6
    column = 0

    with open('./db/menu/main_dishes/main_dishes.txt', 'r') as file:

        for file_line in file:
            if column == 5:
                row += 1
            dish = json.loads(file_line.strip())
            dish_name = dish["name"]
            dish_weight = dish["weight"]
            tk.Button(window,
                      text=f'{dish_name}',
                      bg='#F1B911',
                      height=3,
                      width=11,
                      fg='white',
                      font=('Helvetica', '11'),
                      command=lambda x=dish: order_append(x, current_username, render_main_dishes, window)).grid(row=row, column=column)
            column += 1