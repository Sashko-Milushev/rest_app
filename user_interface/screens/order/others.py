import json
import tkinter as tk

from user_interface.auth_service import get_current_user
from user_interface.util import order_append


def render_others(window):
    current_user = get_current_user()
    current_username = current_user['username']

    row = 12
    column = 0

    with open('./db/menu/others/others.txt', 'r') as file:

        for file_line in file:
            if column == 5:
                row += 1
            other = json.loads(file_line.strip())
            other_name = other["name"]
            drink_weight = other["weight"]
            tk.Button(window,
                      text=f'{other_name}',
                      bg='#DA9641',
                      height=3,
                      width=11,
                      fg='white',
                      font=('Helvetica', '11'),
                      command=lambda x=other: order_append(x, current_username, render_others, window)).grid(
                      row=row, column=column)
            column += 1