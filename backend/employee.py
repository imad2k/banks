import sqlite3
from secrets import token_hex

class Employee:
    dbpath = "banks.db"
    tablename = "Employee"
    
    def __init__(self, **kwargs):
        self.pk = kwargs.get('pk')
        self.employee_id = kwargs.get('employee_id')
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.gender = kwargs.get('gender')
        self.address = kwargs.get('address')
        self.city = kwargs.get('city')
        self.state = kwargs.get('state')
        
    def save(self):
        if self.pk is None:
            self._insert()
        else:
            self._update()
            
    def _insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            SQL = """INSERT INTO {} (employee_id, first_name, last_name, gender, address, city, state) VALUES (?,?,?,?,?,?,?);""".format(self.tablename)
            
            values = (self.employee_id, self.first_name, self.last_name, self.gender, self.address, self.city, self.state)
            
            cursor.execute(SQL, values)
            
    def _update(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            SQL = """UPDATE  {} SET employee_id=?, first_name=?, last_name=?, gender=?, address=?, city=?, state=? WHERE pk=?;""".format(self.tablename)
            
            values = (self.employee_id, self.first_name, self.last_name, self.gender, self.address, self.city, self.state, self.pk)
            
            cursor.execute(SQL, values)
            
    def set_employee_id(self):
        self.employee_id = token_hex(32)
        
        