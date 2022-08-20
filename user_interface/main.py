import tkinter as tk

from user_interface.screens.main_screen import render_main_screen

if __name__ == '__main__':
    window = tk.Tk()
    window.geometry('800x800')
    window.title('restApp')
    render_main_screen(window)
    window.mainloop()