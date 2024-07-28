import tkinter as tk
from tkinter import ttk
from models.air_defense_system import AirDefenseSystem
from models.radar import radars
from models.missile import missiles

class AirDefenseSystemTab:
    def __init__(self, app):
        self.app = app
        self.tab = ttk.Frame(self.app.tab_control)
        self.app.tab_control.add(self.tab, text='Air Defense System')
        
        self.frame = ttk.LabelFrame(self.tab, text='Air Defense Systems')
        self.frame.pack(fill='both', expand='yes', padx=10, pady=10)
        
        self.add_button = ttk.Button(self.frame, text="Add Air Defense System", command=self.add_air_defense_system)
        self.add_button.pack(pady=10)
        
        self.listbox = tk.Listbox(self.frame)
        self.listbox.pack(fill='both', expand='yes', padx=10, pady=10)
        
        self.listbox.bind('<Double-1>', self.show_info)
    
    def add_air_defense_system(self):
        self.window = tk.Toplevel(self.app.root)
        self.window.title("Add Air Defense System")
        self.window.geometry("700x800")  # Adjust size if needed

        self.canvas = tk.Canvas(self.window)
        self.scrollbar = ttk.Scrollbar(self.window, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        
        self.frame = ttk.Frame(self.canvas)
        self.frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.create_widgets()

        self.add_button = ttk.Button(self.frame, text="Add", command=self.save_air_defense_system)
        self.add_button.grid(column=0, row=14, columnspan=2, padx=10, pady=10)
    
    def create_widgets(self):
        ttk.Label(self.frame, text="Name:").grid(column=0, row=0, padx=10, pady=10, sticky='w')
        self.name_entry = ttk.Entry(self.frame)
        self.name_entry.grid(column=1, row=0, padx=10, pady=10, sticky='ew')
        
        ttk.Label(self.frame, text="Radar Names:").grid(column=0, row=1, padx=10, pady=10, sticky='w')
        self.radar_frame = ttk.Frame(self.frame)
        self.radar_frame.grid(column=1, row=1, padx=10, pady=10, sticky='ew')
        
        self.radar_combobox = ttk.Combobox(self.radar_frame, values=list(radars.keys()))
        self.radar_combobox.pack(side=tk.LEFT, padx=5)
        
        self.radar_quantity_entry = ttk.Entry(self.radar_frame, width=5)
        self.radar_quantity_entry.pack(side=tk.LEFT, padx=5)
        
        self.add_radar_button = ttk.Button(self.radar_frame, text="Add Radar", command=self.add_radar)
        self.add_radar_button.pack(side=tk.RIGHT, padx=5)
        
        self.radar_listbox = tk.Listbox(self.frame)
        self.radar_listbox.grid(column=1, row=2, padx=10, pady=10, sticky='ew')
        
        ttk.Label(self.frame, text="Max Aerodynamic Target Range (km):").grid(column=0, row=3, padx=10, pady=10, sticky='w')
        self.aero_range_max_entry = ttk.Entry(self.frame)
        self.aero_range_max_entry.grid(column=1, row=3, padx=10, pady=10, sticky='ew')
        
        ttk.Label(self.frame, text="Min Aerodynamic Target Range (km):").grid(column=0, row=4, padx=10, pady=10, sticky='w')
        self.aero_range_min_entry = ttk.Entry(self.frame)
        self.aero_range_min_entry.grid(column=1, row=4, padx=10, pady=10, sticky='ew')
        
        ttk.Label(self.frame, text="Max Ballistic Target Range (km):").grid(column=0, row=5, padx=10, pady=10, sticky='w')
        self.ballistic_range_max_entry = ttk.Entry(self.frame)
        self.ballistic_range_max_entry.grid(column=1, row=5, padx=10, pady=10, sticky='ew')
        
        ttk.Label(self.frame, text="Min Ballistic Target Range (km):").grid(column=0, row=6, padx=10, pady=10, sticky='w')
        self.ballistic_range_min_entry = ttk.Entry(self.frame)
        self.ballistic_range_min_entry.grid(column=1, row=6, padx=10, pady=10, sticky='ew')
        
        ttk.Label(self.frame, text="Missile Quantities:").grid(column=0, row=7, padx=10, pady=10, sticky='w')
        self.missile_frame = ttk.Frame(self.frame)
        self.missile_frame.grid(column=1, row=7, padx=10, pady=10, sticky='ew')
        
        self.missile_combobox = ttk.Combobox(self.missile_frame, values=list(missiles.keys()))
        self.missile_combobox.pack(side=tk.LEFT, padx=5)
        
        self.missile_quantity_entry = ttk.Entry(self.missile_frame, width=5)
        self.missile_quantity_entry.pack(side=tk.LEFT, padx=5)
        
        self.add_missile_button = ttk.Button(self.missile_frame, text="Add Missile", command=self.add_missile)
        self.add_missile_button.pack(side=tk.RIGHT, padx=5)
        
        self.missile_listbox = tk.Listbox(self.frame)
        self.missile_listbox.grid(column=1, row=8, padx=10, pady=10, sticky='ew')
        
        ttk.Label(self.frame, text="Max Engagements:").grid(column=0, row=9, padx=10, pady=10, sticky='w')
        self.max_engagements_entry = ttk.Entry(self.frame)
        self.max_engagements_entry.grid(column=1, row=9, padx=10, pady=10, sticky='ew')
        
        ttk.Label(self.frame, text="Max Missiles Fired:").grid(column=0, row=10, padx=10, pady=10, sticky='w')
        self.max_missiles_fired_entry = ttk.Entry(self.frame)
        self.max_missiles_fired_entry.grid(column=1, row=10, padx=10, pady=10, sticky='ew')
        
        ttk.Label(self.frame, text="ECM Capability (True/False):").grid(column=0, row=11, padx=10, pady=10, sticky='w')
        self.ecm_capability_entry = ttk.Entry(self.frame)
        self.ecm_capability_entry.grid(column=1, row=11, padx=10, pady=10, sticky='ew')
        
        ttk.Label(self.frame, text="Cost:").grid(column=0, row=12, padx=10, pady=10, sticky='w')
        self.cost_entry = ttk.Entry(self.frame)
        self.cost_entry.grid(column=1, row=12, padx=10, pady=10, sticky='ew')
        
        ttk.Label(self.frame, text="Coordinates (x,y,z):").grid(column=0, row=13, padx=10, pady=10, sticky='w')
        self.coordinates_entry = ttk.Entry(self.frame)
        self.coordinates_entry.grid(column=1, row=13, padx=10, pady=10, sticky='ew')
    
    def add_radar(self):
        radar_name = self.radar_combobox.get()
        quantity = self.radar_quantity_entry.get()
        if radar_name and quantity:
            self.radar_listbox.insert(tk.END, f"{radar_name}: {quantity}")
    
    def add_missile(self):
        missile_name = self.missile_combobox.get()
        quantity = self.missile_quantity_entry.get()
        if missile_name and quantity:
            self.missile_listbox.insert(tk.END, f"{missile_name}: {quantity}")
    
    def save_air_defense_system(self):
        name = self.name_entry.get()
        radar_items = self.radar_listbox.get(0, tk.END)
        radar_names = [item.split(':')[0] for item in radar_items]
        
        aerodynamic_target_range_max = float(self.aero_range_max_entry.get())
        aerodynamic_target_range_min = float(self.aero_range_min_entry.get())
        ballistic_target_range_max = float(self.ballistic_range_max_entry.get())
        ballistic_target_range_min = float(self.ballistic_range_min_entry.get())
        
        missile_items = self.missile_listbox.get(0, tk.END)
        missile_quantities = dict(item.split(':') for item in missile_items)
        missile_quantities = {k: int(v) for k, v in missile_quantities.items()}
        
        max_engagements = int(self.max_engagements_entry.get())
        max_missiles_fired = int(self.max_missiles_fired_entry.get())
        ecm_capability = self.ecm_capability_entry.get() == "True"
        cost = float(self.cost_entry.get())
        coordinates = tuple(map(int, self.coordinates_entry.get().split(',')))
        
        ads = AirDefenseSystem(
            name=name,
            radar_names=radar_names,
            aerodynamic_target_range_max=aerodynamic_target_range_max,
            aerodynamic_target_range_min=aerodynamic_target_range_min,
            ballistic_target_range_max=ballistic_target_range_max,
            ballistic_target_range_min=ballistic_target_range_min,
            missile_quantities=missile_quantities,
            max_engagements=max_engagements,
            max_missiles_fired=max_missiles_fired,
            ecm_capability=ecm_capability,
            cost=cost,
            coordinates=coordinates
        )
        
        self.app.air_defense_systems.append(ads)
        self.listbox.insert(tk.END, ads.name)
        self.window.destroy()
        self.app.update_comboboxes()  # Güncelleme fonksiyonunu `self.app` üzerinden çağırın
    
    def show_info(self, event):
        selected_index = self.listbox.curselection()
        if not selected_index:
            return
        
        selected_index = selected_index[0]
        selected_ads = self.app.air_defense_systems[selected_index]
        info = selected_ads.get_system_info()
        self.app.show_info("Air Defense System Info", info)
    
    def update_comboboxes(self):
        self.radar_combobox['values'] = list(radars.keys())
        self.missile_combobox['values'] = list(missiles.keys())
