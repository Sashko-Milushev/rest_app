import tkinter as tk

from user_interface.screens.login import render_login_screen
from user_interface.screens.register import render_register_screen


def render_main_screen(window):
    tk.Button(window, text='Login', bg='#F1B911', fg='white', command=lambda: render_login_screen(window)).grid(row=0, column=0)

    tk.Button(window, text='Register', bg='green', fg='yellow', command=lambda: render_register_screen(window)).grid(row=0, column=1)







