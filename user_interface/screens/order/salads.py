import json
import tkinter as tk

from user_interface.auth_service import get_current_user
from user_interface.util import order_append


def render_salads(window):
    current_user = get_current_user()
    current_username = current_user['username']

    row = 2
    column = 0


    with open('./db/menu/salads/salads.txt', 'r') as file:
        for file_line in file:
            if column == 5:
                row += 1
            salad = json.loads(file_line.strip())
            salad_name = salad["name"]
            salad_weight = salad["weight"]
            tk.Button(window,
                      text=f'{salad_name}',
                      bg='#98D134',
                      height=3,
                      width=11,
                      fg='white',
                      font=('Helvetica', '11'),
                      command=lambda x=salad_name: order_append(x, render_salads, window)).grid(row=row, column=column)
            column += 1


