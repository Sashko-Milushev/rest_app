def clear_window(window):
    for child in window.winfo_children():
        child.destroy()
