import tkinter as tk

def show_info(app, title, info):
    info_window = tk.Toplevel(app.root)
    info_window.title(title)
    
    text = tk.Text(info_window)
    text.pack(expand=1, fill='both')
    
    def print_dict(d, indent=0):
        for key, value in d.items():
            if isinstance(value, dict):
                text.insert(tk.END, ' ' * indent + str(key) + ":\n")
                print_dict(value, indent + 4)
            elif isinstance(value, list):
                text.insert(tk.END, ' ' * indent + str(key) + ":\n")
                for item in value:
                    print_dict(item, indent + 4)
            else:
                text.insert(tk.END, ' ' * indent + str(key) + ": " + str(value) + "\n")
    
    print_dict(info)
    text.config(state=tk.DISABLED)
