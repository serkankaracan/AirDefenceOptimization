class Missile:
    def __init__(self, name, range_km, speed_mach):
        self.name = name                # Füze adı
        self.range_km = range_km        # Füze menzili (km)
        self.speed_mach = speed_mach    # Füze hızı (mach)

    def get_info(self):
        return {
            "name": self.name,
            "range_km": self.range_km,
            "speed_mach": self.speed_mach,
        }


# Füze tanımları

missiles = {
    "48N6E3": Missile(name="48N6E3", range_km=250, speed_mach=7.5),
    "40N6E": Missile(name="40N6E", range_km=400, speed_mach=9),
    "9M96E": Missile(name="9M96E", range_km=120, speed_mach=3),
    "9M96E2": Missile(name="9M96E2", range_km=120, speed_mach=3),
}
