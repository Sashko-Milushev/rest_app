import tkinter as tk

from user_interface.auth_service import get_current_user
from user_interface.screens.clear_window import clear_window
from user_interface.screens.order.order import render_order


def render_home_screen(window):
    clear_window(window)
    current_user = get_current_user()
    current_username = current_user['username']
    tk.Label(window, text=f'Current user: {current_username}', fg='#F1B911').grid(row=0, column=0)

    tk.Button(window,
              text='Make order',
              bg='#F1B911',
              height=5,
              width=15,
              fg='white',
              font=('Helvetica', '16'),
              command=lambda: render_order(window)).grid(row=2, column=1)

    tk.Button(window,
              text='Change menu',
              bg='#F1B911',
              height=5,
              width=15,
              fg='white',
              font=('Helvetica', '16'),
              command=lambda: print('oredrs')).grid(row=2, column=2)

    tk.Button(window,
              text='Receiving products',
              bg='#F1B911',
              height=5,
              width=15,
              fg='white',
              font=('Helvetica', '16'),
              command=lambda: print('oredrs')).grid(row=2, column=3)