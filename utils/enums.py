from enum import Enum


class IFFStatus(Enum):
    FRIEND = "Friend"            # Dost
    FOE = "Foe"                  # Düşman
    UNKNOWN = "Unknown"          # Bilinmiyor


class AircraftType(Enum):
    FIGHTER = (101, "Fighter")            # Savaş uçağı
    UAV = (102, "UAV")                    # İnsansız hava aracı
    HELICOPTER = (103, "Helicopter")      # Helikopter
    BOMBER = (104, "Bomber")              # Bombardıman uçağı
    TRANSPORT = (105, "Transport")        # Nakliye uçağı
    RECON = (106, "Reconnaissance")       # Keşif uçağı
    ATTACK = (107, "Attack")              # Taarruz uçağı
    TANKER = (108, "Tanker")              # Tanker uçağı
    AWACS = (109, "AWACS")                # Havadan erken uyarı ve kontrol uçağı
    PATROL = (110, "Patrol")              # Devriye uçağı
    TRAINER = (111, "Trainer")            # Eğitim uçağı
    MULTIROLE = (112, "Multirole")        # Çok amaçlı savaş uçağı
    ELECTRONIC_WARFARE = (113, "Electronic Warfare") # Elektronik harp uçağı
    MARITIME_PATROL = (114, "Maritime Patrol")       # Deniz devriye uçağı


class AirDefenseSystemType(Enum):
    SHORT_RANGE = (201, "Short Range")           # Kısa menzil hava savunma sistemi
    MEDIUM_RANGE = (202, "Medium Range")         # Orta menzil hava savunma sistemi
    LONG_RANGE = (203, "Long Range")             # Uzun menzil hava savunma sistemi
    ANTI_MISSILE = (204, "Anti Missile")         # Füze karşıtı hava savunma sistemi
    LASER_DEFENSE = (205, "Laser Defense")       # Lazer savunma sistemi
    ARTILLERY = (206, "Artillery")               # Topçu hava savunma sistemi
    MANPAD = (207, "MANPAD")                     # Taşınabilir hava savunma sistemi (Man-Portable Air-Defense System)
    NAVAL = (208, "Naval")                       # Deniz tabanlı hava savunma sistemi
    MOBILE = (209, "Mobile")                     # Mobil hava savunma sistemi
    STATIC = (210, "Static")                     # Sabit hava savunma sistemi
    SAM = (211, "Surface-to-Air Missile")        # Karadan havaya füze sistemi
    CIWS = (212, "Close-In Weapon System")       # Yakın savunma silah sistemi


class MunitionType(Enum):
    MISSILE = (301, "Missile")                   # Füze
    BOMB = (302, "Bomb")                         # Bomba
    ROCKET = (303, "Rocket")                     # Roket
    BULLET = (304, "Bullet")                     # Mermi
    TORPEDO = (305, "Torpedo")                   # Torpido
    CLUSTER_BOMB = (306, "Cluster Bomb")         # Küme bombası
    NAPALM = (307, "Napalm")                     # Napalm
    NUCLEAR_BOMB = (308, "Nuclear Bomb")         # Nükleer bomba
    GUIDED_MISSILE = (309, "Guided Missile")     # Güdümlü füze
    ANTI_TANK_MISSILE = (310, "Anti-Tank Missile") # Tanksavar füze
    AIR_TO_AIR_MISSILE = (311, "Air-to-Air Missile") # Havadan havaya füze
    AIR_TO_SURFACE_MISSILE = (312, "Air-to-Surface Missile") # Havadan karaya füze


class RadarType(Enum):
    LONG_RANGE_DETECTION = "Long Range Detection"       # Uzun Menzilli Tespit
    MISSILE_GUIDANCE = "Missile Guidance"               # Füze Kılavuzluğu
    LOW_ALTITUDE_DETECTION = "Low Altitude Detection"   # Alçak İrtifa Tespiti
    EARLY_WARNING = "Early Warning"                     # Erken Uyarı
    TARGET_TRACKING = "Target Tracking"                 # Hedef Takibi
    MULTI_FUNCTION = "Multi-Function"                   # Çok İşlevli
    FIRE_CONTROL = "Fire Control"                       # Ateş Kontrol
    SAM_RADAR = "Surface-to-Air Missile (SAM) Radar"    # Yüzeyden Havaya Füze (SAM) Radarı
    AIRBORNE = "Airborne Radar"                         # Hava Radarı

