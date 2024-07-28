from db.database import DatabaseManager
from gui.app import run_app

def main():
    # Veritabanı tablolarını oluştur
    db_manager = DatabaseManager("db/air_defense.db")
    db_manager.create_tables()

    # GUI uygulamasını çalıştır
    run_app()

if __name__ == "__main__":
    main()
