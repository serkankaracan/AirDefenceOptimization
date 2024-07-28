import tkinter as tk
from tkinter import ttk
from models.munition import munitions
from utils.enums import MunitionType

class MunitionTab:
    def __init__(self, app):
        self.app = app
        self.tab = ttk.Frame(self.app.tab_control)
        self.app.tab_control.add(self.tab, text='Munition')
        
        self.frame = ttk.LabelFrame(self.tab, text='Munitions')
        self.frame.pack(fill='both', expand='yes', padx=10, pady=10)
        
        self.add_button = ttk.Button(self.frame, text="Add Munition", command=self.add_munition)
        self.add_button.pack(pady=10)
        
        self.listbox = tk.Listbox(self.frame)
        self.listbox.pack(fill='both', expand='yes', padx=10, pady=10)
        
        self.listbox.bind('<Double-1>', self.show_info)
    
    def add_munition(self):
        self.window = tk.Toplevel(self.app.root)
        self.window.title("Add Munition")
        
        ttk.Label(self.window, text="Name:").grid(column=0, row=0, padx=10, pady=10)
        self.name_entry = ttk.Entry(self.window)
        self.name_entry.grid(column=1, row=0, padx=10, pady=10)
        
        ttk.Label(self.window, text="Type:").grid(column=0, row=1, padx=10, pady=10)
        self.type_combobox = ttk.Combobox(self.window, values=[mtype.name for mtype in MunitionType])
        self.type_combobox.grid(column=1, row=1, padx=10, pady=10)
        
        ttk.Label(self.window, text="Weight (kg):").grid(column=0, row=2, padx=10, pady=10)
        self.weight_entry = ttk.Entry(self.window)
        self.weight_entry.grid(column=1, row=2, padx=10, pady=10)
        
        ttk.Label(self.window, text="Range (km):").grid(column=0, row=3, padx=10, pady=10)
        self.range_entry = ttk.Entry(self.window)
        self.range_entry.grid(column=1, row=3, padx=10, pady=10)
        
        ttk.Label(self.window, text="Explosive Power:").grid(column=0, row=4, padx=10, pady=10)
        self.explosive_power_entry = ttk.Entry(self.window)
        self.explosive_power_entry.grid(column=1, row=4, padx=10, pady=10)
        
        self.add_button = ttk.Button(self.window, text="Add", command=self.save_munition)
        self.add_button.grid(column=0, row=5, columnspan=2, padx=10, pady=10)
    
    def save_munition(self):
        name = self.name_entry.get()
        munition_type = MunitionType[self.type_combobox.get()]
        weight = float(self.weight_entry.get())
        range_km = float(self.range_entry.get())
        explosive_power = float(self.explosive_power_entry.get())
        
        munitions[name] = {
            "name": name,
            "type": munition_type.value,
            "weight": weight,
            "range_km": range_km,
            "explosive_power": explosive_power,
        }
        
        self.listbox.insert(tk.END, name)
        self.window.destroy()
        self.update_comboboxes()
    
    def show_info(self, event):
        selected_index = self.listbox.curselection()[0]
        selected_munition = self.listbox.get(selected_index)
        info = munitions[selected_munition]
        self.app.show_info("Munition Info", info)
    
    def update_comboboxes(self):
        if hasattr(self, 'type_combobox'):
            self.type_combobox['values'] = list(munitions.keys())
