from backend import server as app_instance
from backend import Branch, Employee
import os

PATH = os.path.dirname(__file__)
DATAPATH = os.path.join(PATH, 'data', 'banks.db')
Branch.dbpath = DATAPATH
Employee.dbpath = DATAPATH

app_instance.run(debug=True)

