import json
import tkinter as tk

from user_interface.auth_service import get_current_user
from user_interface.screens.clear_window import clear_window
from user_interface.util import order_append


def render_salads(window):
    clear_window(window)
    current_user = get_current_user()
    current_username = current_user['username']
    tk.Label(window, text=f'Current user: {current_username}', fg='#F1B911').grid(row=0, column=0)
    row = 0
    column = -1

    with open('./db/menu/salads/salads.txt', 'r') as file:
        for file_line in file:
            column += 1
            if column == 2:
                row += 1
            salad = json.loads(file_line.strip())
            salad_name = salad["name"]
            salad_weight = salad["weight"]
            tk.Button(window,
                      text=f'{salad_name}',
                      bg='#F1B911',
                      height=8,
                      width=20,
                      fg='white',
                      font=('Helvetica', '11'),
                      command=lambda x=salad: order_append(x, current_username, render_salads, window)).grid(row=row, column=column)
