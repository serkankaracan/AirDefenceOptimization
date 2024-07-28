from utils.enums import MunitionType

class Munition:
    def __init__(self, name, munition_type, weight, range_km, explosive_power):
        self.name = name  # Mühimmat adı
        self.munition_type = munition_type  # Mühimmat türü (MunitionType)
        self.weight = weight  # kg - Mühimmat ağırlığı
        self.range_km = range_km  # km - Mühimmat menzili
        self.explosive_power = explosive_power  # Mühimmatın patlayıcı gücü (örneğin, TNT eşdeğeri)
        
    def get_info(self):
        return {
            "name": self.name,
            "munition_type": self.munition_type.value,
            "weight": self.weight,
            "range_km": self.range_km,
            "explosive_power": self.explosive_power,
        }

# Mühimmat tanımları
munitions = {
    "AIM-120 AMRAAM": Munition(
        name="AIM-120 AMRAAM",
        munition_type=MunitionType.AIR_TO_AIR_MISSILE,
        weight=152,
        range_km=180,
        explosive_power=10,
    ),
    "GBU-31 JDAM": Munition(
        name="GBU-31 JDAM",
        munition_type=MunitionType.BOMB,
        weight=934,
        range_km=28,
        explosive_power=500,
    ),
    "AGM-65 Maverick": Munition(
        name="AGM-65 Maverick",
        munition_type=MunitionType.AIR_TO_SURFACE_MISSILE,
        weight=300,
        range_km=22,
        explosive_power=135,
    ),
    "Hellfire": Munition(
        name="Hellfire",
        munition_type=MunitionType.AIR_TO_SURFACE_MISSILE,
        weight=49,
        range_km=8,
        explosive_power=9,
    ),
}
