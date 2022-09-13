import json
import tkinter as tk

from user_interface.auth_service import get_current_user
from user_interface.util import order_append


def render_appetizers(window):
    current_user = get_current_user()
    current_username = current_user['username']

    row = 4
    column = 0

    with open('./db/menu/appetizers/appetizers.txt', 'r') as file:
        for file_line in file:
            if column == 5:
                row += 1
            appetizer = json.loads(file_line.strip())
            appetizer_name = appetizer["name"]
            appetizer_weight = appetizer["weight"]
            tk.Button(window,
                      text=f'{appetizer_name}',
                      bg='#34BDD1',
                      height=3,
                      width=11,
                      fg='white',
                      font=('Helvetica', '11'),
                      command=lambda x=appetizer_name: order_append(x, render_appetizers, window)).grid(row=row, column=column)
            column += 1