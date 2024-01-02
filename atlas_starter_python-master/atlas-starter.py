
import json
import random
from urllib import request
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask import Flask, jsonify
from bson import json_util
from flask_cors import CORS
from bson.objectid import ObjectId





app = Flask(__name__)
CORS(app)
uri = "mongodb+srv://harrisibrahim:9876543210@cluster0.z3vfhb9.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))


# @app.route('/autoAddData')
# def add_Data():
#     db = client['mydatabase']
#     collection = db['mycollection']
#     for i in range(100):
#       document = {
#           "name": "Test" + str(random.randint(1, 100)),
#           "age": random.randint(1, 100),
#           "email": str(random.randint(1, 100))+ "@example.com"
#       }
#       result = collection.insert_one(document)
# # print("Inserted document with ID:", result.inserted_id)
#     return 'All data inserted'

@app.route('/deleteEmp')
def delete_emp():
    # db = client['mydatabase']
    # collection = db['mycollection']
    emp_id = request.args.get('empid')
    print(emp_id)
    # query = {"_id": ObjectId(emp_id)}
    # collection.delete_one(query)
 
    return "Deleted"

@app.route('/employess')
def hello_world():
    db = client['mydatabase']
    collection = db['mycollection']
    myData = collection.find({})
    # data_list = list(myData)
    # data_json = json.dumps(data_list)
    # stringified_list = ''.join(data_list)
    return json.loads(json_util.dumps(myData))


if __name__ == '__main__':
    app.run(debug=True)


# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)



document = {
    "name": "Riyas",
    "age": 30,
    "email": "johndoe@example.com"
}

# result = collection.insert_one(document)
# print("Inserted document with ID:", result.inserted_id)
# cursor = collection.find({})
# for document in cursor:
#     print(document)