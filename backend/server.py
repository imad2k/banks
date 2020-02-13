from flask import Flask, request, jsonify
from branch import Branch
from employee import Employee
from flask_cors import CORS
import json




app = Flask(__name__)
CORS(app)


@app.route('/api/v1/branches', methods=["GET"])
def get_branches():
    branches = Branch.select_all()
    # return branches
    # return jsonify({'Bank Branches':branches})
    return jsonify(branches)
    

@app.route('/api/v1/add_branch', methods=['POST'])
def add_branch():
    data = request.get_json()
    # data = json.loads(data2)
    
    city = data["city"]
    state = data['state']
    branch_id = data['branch_id']
    address = data['address']
    new_branch = Branch(branch_id, address, city, state)
    new_branch.save()
    
    return "success"
    
    
    


@app.route('/api/v1/employees/', methods=['GET'])
def get_employees():
    pass
    
    



if __name__ == "__main__":
    app.run(debug=True)