import tkinter as tk
from user_interface.auth_service import register, login


def clear_window(window):
    for child in window.winfo_children():
        child.destroy()


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
        else:
            tk.Label(window, text='Invalid credentials', fg='red').grid(row=2, column=1)

    tk.Button(window, text='Login', bg='orange', fg='white', command=on_login).grid(row=3, column=1)


def render_main_screen(window):
    tk.Button(window, text='Login', bg='orange', fg='white', command=lambda: render_login_screen(window)).grid(row=0, column=0)

    tk.Button(window, text='Register', bg='green', fg='yellow', command=lambda: render_register_screem(window)).grid(row=0, column=1)


def render_register_screem(window):
    clear_window(window)

    tk.Label(window, text='Enter your username: ').grid(row=0, column=0)
    username = tk.Entry(window)
    username.grid(row=0, column=1)

    tk.Label(window, text='Enter your password: ').grid(row=1, column=0)
    password = tk.Entry(window, show='*')
    password.grid(row=1, column=1)

    tk.Label(window, text='Confirm your password: ').grid(row=2, column=0)
    repass = tk.Entry(window, show='*')
    repass.grid(row=2, column=1)

    def on_register():
        username_value = username.get()
        password_value = password.get()
        repass_value = repass.get()

        if password_value != repass_value:
            tk.Label(window, text='Passwords must match!', fg='red').grid(row=3, column=1)
        else:
            result = register(username_value, password_value)
            if result:
                render_login_screen(window)
            else:
                tk.Label(window, text='This username is already used!', fg='red').grid(row=3, column=1)

    tk.Button(window, text='Submit', bg='green', fg='yellow', command=on_register).grid(row=4, column=1)

def render_home_screen(window):
    clear_window(window)


