import psycopg2

class Database:
    def __init__(self):
        self.con = psycopg2.connect(database="flask",
                        host="postgres",
                        user="admin",
                        password="admin",
                        port="5432")
        
    def __del__(self):
        self.con.close()

    def select(self, request, args=[]):
        cursor = self.con.cursor()
        cursor.execute(request, args)

        rows = []
        row = cursor.fetchone()
        while row is not None:
            rows.append(parse_result(cursor, row))
            row = cursor.fetchone()
        return rows

    def select_first(self, request, args=[]):
        cursor = self.con.cursor()
        cursor.execute(request, args)

        return parse_result(cursor, cursor.fetchone())
    
    def insert(self, request, args=[]):
        cursor = self.con.cursor()
        cursor.execute(request, args)
        self.con.commit()
    
    def insert_returning_id(self, request, args=[]):
        cursor = self.con.cursor()
        cursor.execute(request, args)
        self.con.commit()
        return cursor.fetchone()[0]


def parse_result(cursor, row):
    result = None
    if row is not None:
        result = {}
        i = 0
        for col in cursor.description:
            result[col[0]] = row[i]
            i += 1
    return result