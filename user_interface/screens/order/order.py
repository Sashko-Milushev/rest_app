import tkinter as tk

from user_interface.auth_service import get_current_user
from user_interface.screens.clear_window import clear_window
from user_interface.screens.order.appetizers import render_appetizers
from user_interface.screens.order.desserts import render_desserts
from user_interface.screens.order.drinks import render_drinks
from user_interface.screens.order.finish import finish_order
from user_interface.screens.order.main_dishes import render_main_dishes
from user_interface.screens.order.others import render_others
from user_interface.screens.order.salads import render_salads
from user_interface.util import clear_current_order


def render_order(window):
    clear_window(window)
    clear_current_order()
    current_user = get_current_user()
    current_username = current_user['username']
    tk.Label(window, text=f'Current user: {current_username}', fg='#F1B911').grid(row=0, column=0)

    tk.Label(window, text='SALADS:', fg='#98D134', font=('Helvetica', 11, 'bold')).grid(row=1, column=0)
    render_salads(window)

    tk.Label(window, text='APPETIZERS:', fg='#34BDD1', font=('Helvetica', 11, 'bold')).grid(row=3, column=0)
    render_appetizers(window)

    tk.Label(window, text='MAIN DISHES:', fg='#F1B911', font=('Helvetica', 11, 'bold')).grid(row=5, column=0)
    render_main_dishes(window)

    tk.Label(window, text='DESSERTS:', fg='#9834D1', font=('Helvetica', 11, 'bold')).grid(row=7, column=0)
    render_desserts(window)

    tk.Label(window, text='DRINKS:', fg='#2A8A1E', font=('Helvetica', 11, 'bold')).grid(row=9, column=0)
    render_drinks(window)

    tk.Label(window, text='OTHER:', fg='#DA9641', font=('Helvetica', 11, 'bold')).grid(row=11, column=0)
    render_others(window)

    tk.Button(window,
              text=f'FINISH ORDER',
              bg='#C14A1D',
              height=3,
              width=11,
              fg='white',
              font=('Helvetica', '11'),
              command=lambda: finish_order(window, current_username, render_order)).grid(row=13, column=0)


    # tk.Button(window,
    #           text='Appetizers',
    #           bg='#34BDD1',
    #           height=5,
    #           width=11,
    #           fg='white',
    #           font=('Helvetica', '11'),
    #           command=lambda: render_appetizers(window)).grid(row=1, column=2)
    #
    # tk.Button(window,
    #           text='Main dishes',
    #           bg='#F1B911',
    #           height=5,
    #           width=11,
    #           fg='white',
    #           font=('Helvetica', '11'),
    #           command=lambda: print('oredrs')).grid(row=1, column=3)
    #
    # tk.Button(window,
    #           text='Desserts',
    #           bg='#F1B911',
    #           height=5,
    #           width=11,
    #           fg='white',
    #           font=('Helvetica', '11'),
    #           command=lambda: print('oredrs')).grid(row=1, column=4)
    #
    # tk.Button(window,
    #           text='Others',
    #           bg='#F1B911',
    #           height=5,
    #           width=11,
    #           fg='white',
    #           font=('Helvetica', '11'),
    #           command=lambda: print('oredrs')).grid(row=1, column=5)
    #
    # tk.Button(window,
    #           text='Drinks',
    #           bg='#F1B911',
    #           height=5,
    #           width=11,
    #           fg='white',
    #           font=('Helvetica', '11'),
    #           command=lambda: print('oredrs')).grid(row=1, column=6)
