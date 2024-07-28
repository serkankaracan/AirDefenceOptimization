import tkinter as tk
from tkinter import ttk
from models.aircraft import Aircraft
from models.munition import munitions
from models.radar import radars
from utils.enums import AircraftType

class AircraftTab:
    def __init__(self, app):
        self.app = app
        self.tab = ttk.Frame(self.app.tab_control)
        self.app.tab_control.add(self.tab, text='Aircraft')
        
        self.frame = ttk.LabelFrame(self.tab, text='Aircrafts')
        self.frame.pack(fill='both', expand='yes', padx=10, pady=10)
        
        self.add_button = ttk.Button(self.frame, text="Add Aircraft", command=self.add_aircraft)
        self.add_button.pack(pady=10)
        
        self.listbox = tk.Listbox(self.frame)
        self.listbox.pack(fill='both', expand='yes', padx=10, pady=10)
        
        self.listbox.bind('<Double-1>', self.show_info)
    
    def add_aircraft(self):
        self.window = tk.Toplevel(self.app.root)
        self.window.title("Add Aircraft")
        
        ttk.Label(self.window, text="Name:").grid(column=0, row=0, padx=10, pady=10)
        self.name_entry = ttk.Entry(self.window)
        self.name_entry.grid(column=1, row=0, padx=10, pady=10)
        
        ttk.Label(self.window, text="Aircraft Type:").grid(column=0, row=1, padx=10, pady=10)
        self.type_combobox = ttk.Combobox(self.window, values=[atype.name for atype in AircraftType])
        self.type_combobox.grid(column=1, row=1, padx=10, pady=10)
        
        ttk.Label(self.window, text="Speed (Mach):").grid(column=0, row=2, padx=10, pady=10)
        self.speed_entry = ttk.Entry(self.window)
        self.speed_entry.grid(column=1, row=2, padx=10, pady=10)
        
        ttk.Label(self.window, text="Range (km):").grid(column=0, row=3, padx=10, pady=10)
        self.range_entry = ttk.Entry(self.window)
        self.range_entry.grid(column=1, row=3, padx=10, pady=10)
        
        ttk.Label(self.window, text="Max Altitude (km):").grid(column=0, row=4, padx=10, pady=10)
        self.altitude_entry = ttk.Entry(self.window)
        self.altitude_entry.grid(column=1, row=4, padx=10, pady=10)
        
        ttk.Label(self.window, text="Payload Capacity (kg):").grid(column=0, row=5, padx=10, pady=10)
        self.payload_entry = ttk.Entry(self.window)
        self.payload_entry.grid(column=1, row=5, padx=10, pady=10)
        
        ttk.Label(self.window, text="Munitions:").grid(column=0, row=6, padx=10, pady=10)
        self.munition_frame = ttk.Frame(self.window)
        self.munition_frame.grid(column=1, row=6, padx=10, pady=10)
        
        self.add_munition_button = ttk.Button(self.munition_frame, text="Add Munition", command=self.add_munition)
        self.add_munition_button.pack()
        
        self.munition_combobox = ttk.Combobox(self.munition_frame, values=list(munitions.keys()))
        self.munition_combobox.pack(side=tk.LEFT, padx=5)
        
        self.munition_quantity_entry = ttk.Entry(self.munition_frame, width=5)
        self.munition_quantity_entry.pack(side=tk.LEFT, padx=5)
        
        self.munition_listbox = tk.Listbox(self.window)
        self.munition_listbox.grid(column=1, row=7, padx=10, pady=10)
        
        ttk.Label(self.window, text="Radar Names:").grid(column=0, row=8, padx=10, pady=10)
        self.radar_combobox = ttk.Combobox(self.window, values=list(radars.keys()))
        self.radar_combobox.grid(column=1, row=8, padx=10, pady=10)
        
        self.add_button = ttk.Button(self.window, text="Add", command=self.save_aircraft)
        self.add_button.grid(column=0, row=9, columnspan=2, padx=10, pady=10)
    
    def add_munition(self):
        munition_name = self.munition_combobox.get()
        quantity = self.munition_quantity_entry.get()
        if munition_name and quantity:
            self.munition_listbox.insert(tk.END, f"{munition_name}: {quantity}")
    
    def save_aircraft(self):
        name = self.name_entry.get()
        aircraft_type = AircraftType[self.type_combobox.get()]
        speed_mach = float(self.speed_entry.get())
        range_km = float(self.range_entry.get())
        max_altitude_km = float(self.altitude_entry.get())
        payload_capacity_kg = float(self.payload_entry.get())
        munition_items = self.munition_listbox.get(0, tk.END)
        munitions_quantities = dict(item.split(':') for item in munition_items)
        munitions_quantities = {k: int(v) for k, v in munitions_quantities.items()}
        radar_names = self.radar_combobox.get().split(',')
        
        aircraft = Aircraft(
            name=name,
            aircraft_type=aircraft_type,
            speed_mach=speed_mach,
            range_km=range_km,
            max_altitude_km=max_altitude_km,
            payload_capacity_kg=payload_capacity_kg,
            munitions_quantities=munitions_quantities,
            radar_names=radar_names
        )
        
        self.app.aircrafts.append(aircraft)
        self.listbox.insert(tk.END, aircraft.name)
        self.window.destroy()
        self.update_comboboxes()
    
    def show_info(self, event):
        selected_index = self.listbox.curselection()[0]
        selected_aircraft = self.app.aircrafts[selected_index]
        info = selected_aircraft.get_info()
        self.app.show_info("Aircraft Info", info)
    
    def update_comboboxes(self):
        if hasattr(self, 'radar_combobox'):
            self.radar_combobox['values'] = list(radars.keys())
        if hasattr(self, 'munition_combobox'):
            self.munition_combobox['values'] = list(munitions.keys())
