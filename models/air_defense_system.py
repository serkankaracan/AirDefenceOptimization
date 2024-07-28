from models.missile import missiles
from models.radar import radars

class AirDefenseSystem:
    def __init__(
        self,
        name,
        radar_names,
        aerodynamic_target_range_max,
        aerodynamic_target_range_min,
        ballistic_target_range_max,
        ballistic_target_range_min,
        missile_quantities,
        max_engagements,
        max_missiles_fired,
        ecm_capability,
        cost,
        coordinates
    ):
        self.name = name  # Sistemin adı
        self.radars = [radars[radar_name] for radar_name in radar_names]  # Radar nesneleri
        self.aerodynamic_target_range_max = aerodynamic_target_range_max  # km - Aerodinamik hedeflere karşı maksimum menzil
        self.aerodynamic_target_range_min = aerodynamic_target_range_min  # km - Aerodinamik hedeflere karşı minimum menzil
        self.ballistic_target_range_max = ballistic_target_range_max  # km - Balistik hedeflere karşı maksimum menzil
        self.ballistic_target_range_min = ballistic_target_range_min  # km - Balistik hedeflere karşı minimum menzil
        self.missile_quantities = missile_quantities  # Füze tipleri ve miktarları
        self.max_engagements = max_engagements  # Aynı anda angaje olabileceği hedef sayısı
        self.max_missiles_fired = max_missiles_fired  # Aynı anda fırlatılabilecek füze sayısı
        self.ecm_capability = ecm_capability  # Elektronik harp yetenekleri (True/False)
        self.cost = cost  # Sistem maliyeti
        self.coordinates = coordinates  # Koordinatlar (x, y, z)

    def get_system_info(self):
        missiles_info = {
            name: {"info": missiles[name].get_info(), "quantity": quantity}
            for name, quantity in self.missile_quantities.items()
        }
        radars_info = [radar.get_info() for radar in self.radars]
        return {
            "name": self.name,
            "radars": radars_info,  # Radar bilgileri
            "aerodynamic_target_range_max": self.aerodynamic_target_range_max,  # km - Aerodinamik hedeflere karşı maksimum menzil
            "aerodynamic_target_range_min": self.aerodynamic_target_range_min,  # km - Aerodinamik hedeflere karşı minimum menzil
            "ballistic_target_range_max": self.ballistic_target_range_max,  # km - Balistik hedeflere karşı maksimum menzil
            "ballistic_target_range_min": self.ballistic_target_range_min,  # km - Balistik hedeflere karşı minimum menzil
            "missiles": missiles_info,  # Füze bilgileri ve miktarları
            "max_engagements": self.max_engagements,  # Aynı anda angaje olabileceği hedef sayısı
            "max_missiles_fired": self.max_missiles_fired,  # Aynı anda fırlatılabilecek füze sayısı
            "ecm_capability": self.ecm_capability,  # Elektronik harp yetenekleri (True/False)
            "cost": self.cost,  # Sistem maliyeti
            "coordinates": self.coordinates  # Koordinatlar (x, y, z)
        }
