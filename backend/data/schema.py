import sqlite3
import os


DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR, 'banks.db')

def schema(dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        cursor = conn.cursor()
    
        SQL = """CREATE TABLE Branch(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            branch_id VARCHAR(32),
            address VARCHAR(32),
            city VARCHAR(32),
            state VARCHAR(32)
        );"""
        
        cursor.execute(SQL)
        
        SQL = """CREATE TABLE Employee(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id VARCHAR(32),
            first_name VARCHAR(32),
            last_name VARCHAR(32),
            gender VARCHAR(6),
            address VARCHER(32),
            city VARCHAR(32),
            state VARCHAR(32),
            FOREIGN KEY (employee_id) REFERENCES Branch(pk)
        );"""
        
        cursor.execute(SQL)
        
if __name__ == '__main__':
    schema()