import sqlite3
from sqlite3 import Error
from pathlib import Path
import time

import random as rnd

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def add_row(conn, record):

    currtime = time.time() * 1000000000

    record.insert(0, currtime);

    sql = ''' INSERT INTO records('currtime', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140')
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''

    cur = conn.cursor()
    cur.execute(sql, record)
    conn.commit()

def get_records():
    
    database = Path("./db/sqlite.db")
    conn = create_connection(database)

    cur = conn.cursor()
    cur.execute("SELECT * FROM records")

    rows = cur.fetchall()

    return rows;

def add_jitter(record):

    newrecord = []

    for el in record:
        newrecord.append(el + el*(rnd.uniform(0.1, 0.2)))
     
    return newrecord


def store_record(record):
    # database = r"C:\sqlite\db\pythonsqlite.db"

    database = Path("./db/sqlite.db")

    sql_create_records_table = """ CREATE TABLE IF NOT EXISTS records (
                                        id integer PRIMARY KEY,
                                        'currtime' integer,
                                        '101' integer, '102' integer, '103' integer, '104' integer, '105' integer, '106' integer, '107' integer, '108' integer, '109' integer, '110' integer, '111' integer, '112' integer, '113' integer, '114' integer, '115' integer, '116' integer, '117' integer, '118' integer, '119' integer, '120' integer, '121' integer, '122' integer, '123' integer, '124' integer, '125' integer, '126' integer, '127' integer, '128' integer, '129' integer, '130' integer, '131' integer, '132' integer, '133' integer, '134' integer, '135' integer, '136' integer, '137' integer, '138' integer, '139' integer, '140' integer
                                    ); """

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_records_table)

        add_row(conn, add_jitter(record));





    else:
        print("Error! cannot create the database connection.")
