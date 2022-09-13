import tkinter as tk

from user_interface.screens.main_screen import render_main_screen


def main():
    window = tk.Tk()
    # window.attributes('-fullscreen', True)
    window.geometry('1200x1200')
    window.title('restApp')
    render_main_screen(window)
    window.mainloop()


if __name__ == '__main__':
    main()
