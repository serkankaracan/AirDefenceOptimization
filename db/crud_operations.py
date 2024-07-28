class CRUDOperations:
    def __init__(self, conn):
        self.conn = conn

    def insert_radar(self, radar):
        sql = ''' INSERT INTO radar(name, range_max, range_min, type)
                  VALUES(?,?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, radar)
        self.conn.commit()
        return cur.lastrowid

    def insert_munition(self, munition):
        sql = ''' INSERT INTO munition(name, type, destructive_power)
                  VALUES(?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, munition)
        self.conn.commit()
        return cur.lastrowid

    def insert_missile(self, missile):
        sql = ''' INSERT INTO missile(name, type, range, speed)
                  VALUES(?,?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, missile)
        self.conn.commit()
        return cur.lastrowid

    def insert_aircraft(self, aircraft):
        sql = ''' INSERT INTO aircraft(name, type, speed, range, maneuverability)
                  VALUES(?,?,?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, aircraft)
        self.conn.commit()
        return cur.lastrowid

    def insert_ads(self, ads):
        sql = ''' INSERT INTO air_defense_system(name, radar_ids, missile_ids, max_engagements, max_missiles_fired, ecm_capability, cost, coordinates)
                  VALUES(?,?,?,?,?,?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, ads)
        self.conn.commit()
        return cur.lastrowid
