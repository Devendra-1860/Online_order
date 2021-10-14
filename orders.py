from sql_connection import sql_connection
from datetime import datetime

def insert_order(connector, order):  #Inserts order into the database
    cursor = connector.cursor()

    query = ("INSERT INTO orders "
             "(customer, total_amount, time)"
             "VALUES (%s, %s, %s)")
    data = (order['customer'], order['total_amount'], datetime.now())

    cursor.execute(query, data)
    order_id = cursor.lastrowid   #Gets the last row id in the order table, this can be used to inserting order details in order_details table 

    order_details_query = ("INSERT INTO order_details "
                           "(order_id, item_id, quantity, total_price)"
                           "VALUES (%s, %s, %s, %s)")

    order_details_data = []
    for order_detail_record in order['order_details']:
        order_details_data.append((
            order_id,
            int(order_detail_record['item_id']),
            float(order_detail_record['quantity']),
            float(order_detail_record['total_price'])
        ))
    cursor.executemany(order_details_query, order_details_data)  #Used to insert multiple rows in the order details table

    connector.commit()
    return order_id
    
def order_details(connector, order_id):  #Shows all the order details
    cursor = connector.cursor()

    #query = "SELECT * from order_details where order_id = %s"

    query = "SELECT order_details.order_id, order_details.quantity, order_details.total_price, "\
            "items.item_name, items.item_price FROM order_details LEFT JOIN items on " \
            "order_details.item_id = items.item_id where order_details.order_id = %s"
    # left join query to show the order details for a particular order_id
    data = (order_id, )

    cursor.execute(query, data)

    records = []
    for (order_id, quantity, total_price, item_name, item_price) in cursor:
        records.append({
            'order_id': order_id,
            'quantity': quantity,
            'total_price': total_price,
            'item_name': item_name,
            'item_price': item_price
        })

    cursor.close()

    return records

if __name__ == '__main__':
    connector = sql_connection()
    '''print(insert_order(connector, order = {'customer': 'Devendra','total_amount': '170','time': datetime.now(),
         'order_details': [
             {
                 'item_id': 1,
                 'quantity': 3,
                 'total_price': 120
             },
             {
                 'item_id': 4,
                 'quantity': 1,
                 'total_price': 50
             }
         ]
     }))''' #inserting order
    #print(order_details(connector, order_id=1))

