from flask import Flask, request, jsonify
import items
from sql_connection import sql_connection
import orders
import json

app = Flask(__name__)
connector = sql_connection()


user_pass = {'Devendra':'1860', 'Gowtham':'1500','Pavan':'1300'}  #users credentials
@app.route('/loginpage')
def login():  #Checks for correct login credentials
    user_name = request.form['username'] #asking username from users
    password = request.form['password']  #asking for password
    if user_name not in user_pass:
        return 'Wrong username'
    else:
        if user_pass[user_name] != password:
            return 'Wrong password'
        else:
            return 'Go to Homepage'

@app.route('/showitems', methods=['GET'])
def get_items():   #Shows all the items availiable
    response = items.all_items(connector)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/insertitem', methods=['POST'])
def insert_item():   #Inserts new item 
    request_payload = json.loads(request.form['data'])
    item_id = items.insert_new_item(connector, request_payload)
    response = jsonify({'item_id': item_id})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/deleteitem', methods=['POST'])
def delete_item():   #Deletes an item
    return_id = items.delete_item(connector, request.form['item_id'])
    response = jsonify({'product_id': return_id})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertorder', methods=['POST'])
def insert_order():    #Ordering items
    request_payload = json.loads(request.form['data'])
    order_id = orders.insert_order(connector, request_payload)
    response = jsonify({'order_id': order_id})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/showallorders', methods=['GET'])
def show_all_orders():   #Shows all the orders
    response = orders.all_orders(connector)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    app.run(port=1000)