import sqlite3


class DatabaseManager:
    def __init__(self, db_file):
        """Veritabanına bağlantı kurar."""
        self.conn = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Veritabanına bağlantı kurar."""
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except sqlite3.Error as e:
            print(e)
        return None

    def create_table(self, create_table_sql):
        """Bir tablo oluşturur."""
        try:
            c = self.conn.cursor()
            c.execute(create_table_sql)
        except sqlite3.Error as e:
            print(e)

    def create_tables(self):
        sql_create_radar_table = """ CREATE TABLE IF NOT EXISTS radar (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        range_max integer,
                                        range_min integer,
                                        type text
                                    ); """

        sql_create_munition_table = """CREATE TABLE IF NOT EXISTS munition (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    type text,
                                    destructive_power integer
                                );"""

        sql_create_missile_table = """CREATE TABLE IF NOT EXISTS missile (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    type text,
                                    range integer,
                                    speed integer
                                );"""

        sql_create_aircraft_table = """CREATE TABLE IF NOT EXISTS aircraft (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    type text,
                                    speed integer,
                                    range integer,
                                    maneuverability integer
                                );"""

        sql_create_ads_table = """CREATE TABLE IF NOT EXISTS air_defense_system (
                                id integer PRIMARY KEY,
                                name text NOT NULL,
                                radar_ids text,
                                missile_ids text,
                                max_engagements integer,
                                max_missiles_fired integer,
                                ecm_capability text,
                                cost integer,
                                coordinates text
                            );"""

        if self.conn is not None:
            self.create_table(sql_create_radar_table)
            self.create_table(sql_create_munition_table)
            self.create_table(sql_create_missile_table)
            self.create_table(sql_create_aircraft_table)
            self.create_table(sql_create_ads_table)
        else:
            print("Error! Cannot create the database connection.")
