import sqlite3
from secrets import token_hex


class Branch:
    dbpath = "banks.db"
    tablename = 'Branch'
    
    # def __init__(self, **kwargs):
    #     self.pk = kwargs.get('pk')
    #     self.branch_id = kwargs.get('branch_id')
    #     self.address = kwargs.get('address')
    #     self.city = kwargs.get('city')
    #     self.state = kwargs.get('state')
        
    def __init__(self, branch_id, address, city, state):
        
        self.branch_id = branch_id
        self.address = address
        self.city = city
        self.state = state
        
    
    def save(self):
        self._insert()
        
        # if self.pk is None:
        #     self._insert()
        # else:
        #     self._update()
            
    def _insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            
            SQL = """INSERT INTO {}(branch_id, address, city, state) VALUES (?,?,?,?);""".format(self.tablename)
            
            values = (self.branch_id, self.address, self.city, self.state)
            cursor.execute(SQL, values)
            
    def _update(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            
            SQL = """UPDATE {} SET branch_id=?, address=?, city=?, state=?) WHERE pk=?;""".format(self.tablename)
            
            values = (self.branch_id, self.address, self.city, self.state, self.pk)
            cursor.execute(SQL, values)
            
    def set_branch_id(self):
        self.branch_id = token_hex(2)
    
    
    @classmethod
    def select_all(cls):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            SQL = """SELECT * FROM Branch;"""
            
            cursor.execute(SQL)
            branches = cursor.fetchall()
            fields = ['pk', 'branch_id', 'address', 'city', 'state']
            dicts = [dict(zip(fields, d)) for d in branches]
            
            return dicts
            
        