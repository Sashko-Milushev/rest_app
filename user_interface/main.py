import tkinter as tk

from user_interface.screens import render_main_screen

if __name__ == '__main__':
    window = tk.Tk()
    window.geometry('700x700')
    window.title('restApp')
    render_main_screen(window)
    window.mainloop()