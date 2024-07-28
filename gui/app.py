import tkinter as tk
from tkinter import ttk
from gui.air_defense_system_tab import AirDefenseSystemTab
from gui.aircraft_tab import AircraftTab
from gui.munition_tab import MunitionTab
from gui.missile_tab import MissileTab
from gui.radar_tab import RadarTab

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Defense System GUI")
        
        self.air_defense_systems = []
        self.aircrafts = []
        
        # Tab Control
        self.tab_control = ttk.Notebook(root)
        
        # Initialize Tabs
        self.ads_tab = AirDefenseSystemTab(self)
        self.aircraft_tab = AircraftTab(self)
        self.munition_tab = MunitionTab(self)
        self.missile_tab = MissileTab(self)
        self.radar_tab = RadarTab(self)
        
        self.tab_control.pack(expand=1, fill='both')
    
    def update_comboboxes(self):
        self.ads_tab.update_comboboxes()
        self.aircraft_tab.update_comboboxes()

    def show_info(self, title, message):
        info_window = tk.Toplevel(self.root)
        info_window.title(title)
        info_window.geometry("400x300")  # Pencere boyutunu ihtiyaçlarınıza göre ayarlayın
        
        # Pencere içeriğini düzenli ve okunaklı hale getirme
        info_frame = ttk.Frame(info_window)
        info_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        info_label = ttk.Label(info_frame, text=message, justify=tk.LEFT)
        info_label.pack(side=tk.TOP, fill='both', expand=True)
        
        # Daha estetik bir görünüm için metin alanı kullanılabilir
        text_widget = tk.Text(info_frame, wrap=tk.WORD, height=15, width=50)
        text_widget.insert(tk.END, message)
        text_widget.configure(state=tk.DISABLED)  # Metni düzenlemeyi engelle
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Scrollbar ekleyin
        scrollbar = ttk.Scrollbar(info_frame, orient=tk.VERTICAL, command=text_widget.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text_widget.config(yscrollcommand=scrollbar.set)
        
        # Kapatma butonu ekleyin
        close_button = ttk.Button(info_frame, text="Close", command=info_window.destroy)
        close_button.pack(side=tk.BOTTOM, pady=10)


def run_app():
    root = tk.Tk()
    app = App(root)
    app.root.mainloop()
