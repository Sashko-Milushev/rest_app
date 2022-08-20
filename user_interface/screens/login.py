import tkinter as tk

from user_interface.auth_service import login
from user_interface.screens.home import render_home_screen
from user_interface.screens.clear_window import clear_window
from user_interface.util import clear_current_order


def render_login_screen(window):
    clear_window(window)

    tk.Label(window, text='Enter your username: ').grid(row=0, column=0)
    username = tk.Entry(window)
    username.grid(row=0, column=1)

    tk.Label(window, text='Enter your password: ').grid(row=1, column=0)
    password = tk.Entry(window, show='*')
    password.grid(row=1, column=1)

    def on_login():
        username_value = username.get()
        password_value = password.get()

        result = login(username_value, password_value)
        if result:
            render_home_screen(window)
            clear_current_order()
        else:
            tk.Label(window, text='Invalid credentials', fg='red').grid(row=2, column=1)

    tk.Button(window, text='Login', bg='#F1B911', fg='white', command=on_login).grid(row=3, column=1)

