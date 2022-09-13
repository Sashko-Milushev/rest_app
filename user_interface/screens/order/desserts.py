import json
import tkinter as tk

from user_interface.auth_service import get_current_user
from user_interface.util import order_append


def render_desserts(window):
    current_user = get_current_user()
    current_username = current_user['username']

    row = 8
    column = 0

    with open('./db/menu/desserts/desserts.txt', 'r') as file:

        for file_line in file:
            if column == 5:
                row += 1
            dessert = json.loads(file_line.strip())
            dessert_name = dessert["name"]
            dish_weight = dessert["weight"]
            tk.Button(window,
                      text=f'{dessert_name}',
                      bg='#9834D1',
                      height=3,
                      width=11,
                      fg='white',
                      font=('Helvetica', '11'),
                      command=lambda x=dessert_name: order_append(x, render_desserts, window)).grid(
                      row=row, column=column)
            column += 1