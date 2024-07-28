import tkinter as tk
from tkinter import ttk
from models.radar import radars, Radar
from utils.enums import RadarType

class RadarTab:
    def __init__(self, app):
        self.app = app
        self.tab = ttk.Frame(self.app.tab_control)
        self.app.tab_control.add(self.tab, text='Radar')
        
        self.frame = ttk.LabelFrame(self.tab, text='Radars')
        self.frame.pack(fill='both', expand='yes', padx=10, pady=10)
        
        self.add_button = ttk.Button(self.frame, text="Add Radar", command=self.add_radar)
        self.add_button.pack(pady=10)
        
        self.listbox = tk.Listbox(self.frame)
        self.listbox.pack(fill='both', expand='yes', padx=10, pady=10)
        
        self.listbox.bind('<Double-1>', self.show_info)
    
    def add_radar(self):
        self.window = tk.Toplevel(self.app.root)
        self.window.title("Add Radar")
        
        ttk.Label(self.window, text="Name:").grid(column=0, row=0, padx=10, pady=10)
        self.name_entry = ttk.Entry(self.window)
        self.name_entry.grid(column=1, row=0, padx=10, pady=10)
        
        ttk.Label(self.window, text="Type:").grid(column=0, row=1, padx=10, pady=10)
        self.type_combobox = ttk.Combobox(self.window, values=[rtype.name for rtype in RadarType])
        self.type_combobox.grid(column=1, row=1, padx=10, pady=10)
        
        ttk.Label(self.window, text="Detection Range (km):").grid(column=0, row=2, padx=10, pady=10)
        self.range_entry = ttk.Entry(self.window)
        self.range_entry.grid(column=1, row=2, padx=10, pady=10)
        
        ttk.Label(self.window, text="Max Altitude (km):").grid(column=0, row=3, padx=10, pady=10)
        self.altitude_max_entry = ttk.Entry(self.window)
        self.altitude_max_entry.grid(column=1, row=3, padx=10, pady=10)
        
        ttk.Label(self.window, text="Min Altitude (km):").grid(column=0, row=4, padx=10, pady=10)
        self.altitude_min_entry = ttk.Entry(self.window)
        self.altitude_min_entry.grid(column=1, row=4, padx=10, pady=10)
        
        ttk.Label(self.window, text="Max Target Speed (km/s):").grid(column=0, row=5, padx=10, pady=10)
        self.speed_max_entry = ttk.Entry(self.window)
        self.speed_max_entry.grid(column=1, row=5, padx=10, pady=10)
        
        ttk.Label(self.window, text="Max Target Velocity (km/h):").grid(column=0, row=6, padx=10, pady=10)
        self.velocity_max_entry = ttk.Entry(self.window)
        self.velocity_max_entry.grid(column=1, row=6, padx=10, pady=10)
        
        ttk.Label(self.window, text="Redeployment Time (s):").grid(column=0, row=7, padx=10, pady=10)
        self.redeployment_entry = ttk.Entry(self.window)
        self.redeployment_entry.grid(column=1, row=7, padx=10, pady=10)
        
        self.add_button = ttk.Button(self.window, text="Add", command=self.save_radar)
        self.add_button.grid(column=0, row=8, columnspan=2, padx=10, pady=10)
    
    def save_radar(self):
        name = self.name_entry.get()
        radar_type = RadarType[self.type_combobox.get()]
        detection_range = float(self.range_entry.get())
        max_altitude = float(self.altitude_max_entry.get())
        min_altitude = float(self.altitude_min_entry.get())
        max_target_speed = float(self.speed_max_entry.get())
        max_target_velocity = float(self.velocity_max_entry.get())
        redeployment_time = float(self.redeployment_entry.get())
        
        radars[name] = Radar(
            name=name,
            radar_type=radar_type,
            detection_range=detection_range,
            max_altitude=max_altitude,
            min_altitude=min_altitude,
            max_target_speed=max_target_speed,
            max_target_velocity=max_target_velocity,
            redeployment_time=redeployment_time,
        )
        
        self.listbox.insert(tk.END, name)
        self.window.destroy()
        self.update_comboboxes()
    
    def show_info(self, event):
        selected_index = self.listbox.curselection()[0]
        selected_radar = self.listbox.get(selected_index)
        info = radars[selected_radar].get_info()
        self.app.show_info("Radar Info", info)
    
    def update_comboboxes(self):
        if hasattr(self, 'listbox'):
            self.listbox['values'] = list(radars.keys())
