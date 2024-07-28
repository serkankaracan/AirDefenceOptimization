from utils.enums import RadarType


class Radar:
    def __init__(
        self,
        name,
        radar_type,
        detection_range,
        max_altitude,
        min_altitude,
        max_target_speed,
        max_target_velocity,
        redeployment_time,
    ):
        self.name = name  # Radar adı
        self.radar_type = radar_type
        self.detection_range = detection_range  # km - Radarın tespit mesafesi
        self.max_altitude = max_altitude  # km - Radarın tespit edebileceği maksimum irtifa
        self.min_altitude = min_altitude  # km - Radarın tespit edebileceği minimum irtifa
        self.max_target_speed = max_target_speed  # km/s - Radarın tespit edebileceği maksimum hedef hızı
        self.max_target_velocity = max_target_velocity  # km/h - Radarın tespit edebileceği maksimum hedef hızı (diğer birimle)
        self.redeployment_time = redeployment_time  # Saniye cinsinden - Radarın yeniden konuşlandırılma süresi

    def get_info(self):
        return {
            "name": self.name,
            "radar_type": self.radar_type.value,
            "detection_range": self.detection_range,
            "max_altitude": self.max_altitude,
            "min_altitude": self.min_altitude,
            "max_target_speed": self.max_target_speed,
            "max_target_velocity": self.max_target_velocity,
            "redeployment_time": self.redeployment_time,
        }


# Radar tanımları
radars = {
    "92N6E": Radar(
        name="92N6E",
        radar_type=RadarType.MISSILE_GUIDANCE,
        detection_range=600,
        max_altitude=30,
        min_altitude=0.01,
        max_target_speed=4.8,
        max_target_velocity=17000,
        redeployment_time=300,
    ),
    "91N6E": Radar(
        name="91N6E",
        radar_type=RadarType.LONG_RANGE_DETECTION,
        detection_range=400,
        max_altitude=27,
        min_altitude=0.01,
        max_target_speed=4.8,
        max_target_velocity=17000,
        redeployment_time=300,
    ),
    "96L6E": Radar(
        name="96L6E",
        radar_type=RadarType.LOW_ALTITUDE_DETECTION,
        detection_range=100,
        max_altitude=20,
        min_altitude=0.01,
        max_target_speed=3.0,
        max_target_velocity=11000,
        redeployment_time=300,
    ),
}
