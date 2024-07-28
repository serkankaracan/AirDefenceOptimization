from models.munition import munitions
from models.radar import radars

class Aircraft:
    def __init__(
        self,
        name,
        aircraft_type,
        speed_mach,
        range_km,
        max_altitude_km,
        payload_capacity_kg,
        munitions_quantities,
        radar_names,
    ):
        self.name = name  # Uçağın adı
        self.aircraft_type = aircraft_type  # Uçak tipi (AircraftType)
        self.speed_mach = speed_mach  # Mach - Uçağın hızı
        self.range_km = range_km  # km - Uçağın menzili
        self.max_altitude_km = max_altitude_km  # km - Uçağın maksimum irtifası
        self.payload_capacity_kg = payload_capacity_kg  # kg - Uçağın taşıyabileceği maksimum yük
        self.munitions_quantities = munitions_quantities  # Mühimmat türleri ve miktarları
        self.radars = [radars[radar_name] for radar_name in radar_names]  # Radar nesneleri
        
    def get_info(self):
        munitions_info = {
            munition_type: {
                "info": munitions[munition_type].get_info(),
                "quantity": quantity,
            }
            for munition_type, quantity in self.munitions_quantities.items()
        }
        radars_info = [radar.get_info() for radar in self.radars]
        return {
            "name": self.name,
            "aircraft_type": self.aircraft_type.value,
            "speed_mach": self.speed_mach,
            "range_km": self.range_km,
            "max_altitude_km": self.max_altitude_km,
            "payload_capacity_kg": self.payload_capacity_kg,
            "munitions": munitions_info,
            "radars": radars_info,  # Radar bilgileri
        }
