import mysql.connector


def execute (query):
    try:
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="logsSport"
        )

        cursor = db_connection.cursor()

        cursor.execute(query)
        rows = cursor.fetchall()
        db_connection.close()
        return rows
    except Exception:
        return False

def save(query):
    try:
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="logsSport"
        )
        cursor = db_connection.cursor()

        cursor.execute(query)
        db_connection.commit()
        
        return True
    except Exception:
        return False