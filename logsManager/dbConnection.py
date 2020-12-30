import mysql.connector
import os
import sys
import json

def readCredentials():
    basedir = os.path.dirname(sys.modules['__main__'].__file__)
    files = [f for f in os.listdir(basedir) if os.path.isfile(f)]
    if 'credentialsDB.json' in files:
        with open(basedir+'/credentialsDB.json') as credentials:
            return json.load(credentials)
    else:
        raise IOError('File not found')

def execute (query):
    try:
        credentials = readCredentials()
        db_connection = mysql.connector.connect(
            host=credentials['host'],
            user=credentials['user'],
            password=credentials['password'],
            database=credentials['database']
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
        credentials = readCredentials()
        db_connection = mysql.connector.connect(
            host=credentials['host'],
            user=credentials['user'],
            password=credentials['password'],
            database=credentials['database']
        )
        cursor = db_connection.cursor()

        cursor.execute(query)
        db_connection.commit()
        
        return True
    except Exception:
        return False