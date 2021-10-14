from sql_connection import sql_connection


def insert_new_item(connector, item):
    cursor = connector.cursor()
    query = ("INSERT INTO items"
             "(item_name, item_price)"
             "VALUES (%s, %s)")
    data = (item['item_name'], item['item_price'])
    cursor.execute(query,data)
    connector.commit()
    
    return cursor.lastrowid

def delete_item(connector, item_id):
    cursor = connector.cursor()
    query = ("DELETE FROM items where item_id = "+ str(item_id))
    cursor.execute(query)
    connector.commit()
    return cursor.lastrowid

def all_items(connector):
    
    
    cursor = connector.cursor()
    query = 'SELECT * FROM online_order.items'
    
    cursor.execute(query)
    
    all_items = []
    
    for (item_id, item_name, item_price) in cursor:
        all_items.append({'item_id':item_id, 'item_name':item_name, 'item_price':item_price})
        
    
    return all_items

    
if __name__ == '__main__':
    connector = sql_connection()
    #print(all_items(connector))
    print(insert_new_item(connector, item = {'item_name':'soap', 'item_price':40}))
    #print(delete_item(connector, item_id= 4))
    print(all_items(connector))