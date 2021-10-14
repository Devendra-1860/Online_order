import mysql.connector

__cnx = None

def sql_connection():
    global __cnx
    if __cnx is None:  #to make sure that all the previous connections are removed
        __cnx = mysql.connector.connect(user = 'root', password = 'Devendr@1860',
                                  host = '127.0.0.1', database = 'online_order')
    return __cnx

# In the online_order database there are three tables. 1. items, 2. orders, 3. order_details