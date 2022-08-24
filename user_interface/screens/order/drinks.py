import json
import tkinter as tk

from user_interface.auth_service import get_current_user
from user_interface.util import order_append


def render_drinks(window):
    current_user = get_current_user()
    current_username = current_user['username']

    row = 10
    column = 0

    with open('./db/menu/drinks/drinks.txt', 'r') as file:

        for file_line in file:
            if column == 5:
                row += 1
            drink = json.loads(file_line.strip())
            drink_name = drink["name"]
            drink_weight = drink["weight"]
            tk.Button(window,
                      text=f'{drink_name}',
                      bg='#2A8A1E',
                      height=3,
                      width=11,
                      fg='white',
                      font=('Helvetica', '11'),
                      command=lambda x=drink: order_append(x, current_username, render_drinks, window)).grid(
                      row=row, column=column)
            column += 1