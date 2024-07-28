import tkinter as tk
from tkinter import ttk
from models.missile import missiles

class MissileTab:
    def __init__(self, app):
        self.app = app
        self.tab = ttk.Frame(self.app.tab_control)
        self.app.tab_control.add(self.tab, text='Missile')
        
        self.frame = ttk.LabelFrame(self.tab, text='Missiles')
        self.frame.pack(fill='both', expand='yes', padx=10, pady=10)
        
        self.add_button = ttk.Button(self.frame, text="Add Missile", command=self.add_missile)
        self.add_button.pack(pady=10)
        
        self.listbox = tk.Listbox(self.frame)
        self.listbox.pack(fill='both', expand='yes', padx=10, pady=10)
        
        self.listbox.bind('<Double-1>', self.show_info)
    
    def add_missile(self):
        self.window = tk.Toplevel(self.app.root)
        self.window.title("Add Missile")
        
        ttk.Label(self.window, text="Name:").grid(column=0, row=0, padx=10, pady=10)
        self.name_entry = ttk.Entry(self.window)
        self.name_entry.grid(column=1, row=0, padx=10, pady=10)
        
        ttk.Label(self.window, text="Range (km):").grid(column=0, row=1, padx=10, pady=10)
        self.range_entry = ttk.Entry(self.window)
        self.range_entry.grid(column=1, row=1, padx=10, pady=10)
        
        ttk.Label(self.window, text="Speed (Mach):").grid(column=0, row=2, padx=10, pady=10)
        self.speed_entry = ttk.Entry(self.window)
        self.speed_entry.grid(column=1, row=2, padx=10, pady=10)
        
        self.add_button = ttk.Button(self.window, text="Add", command=self.save_missile)
        self.add_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)
    
    def save_missile(self):
        name = self.name_entry.get()
        range_km = float(self.range_entry.get())
        speed_mach = float(self.speed_entry.get())
        
        missiles[name] = {
            "name": name,
            "range_km": range_km,
            "speed_mach": speed_mach,
        }
        
        self.listbox.insert(tk.END, name)
        self.window.destroy()
        self.update_comboboxes()
    
    def show_info(self, event):
        selected_index = self.listbox.curselection()[0]
        selected_missile = self.listbox.get(selected_index)
        info = missiles[selected_missile]
        self.app.show_info("Missile Info", info)
    
    def update_comboboxes(self):
        if hasattr(self, 'listbox'):
            self.listbox['values'] = list(missiles.keys())
