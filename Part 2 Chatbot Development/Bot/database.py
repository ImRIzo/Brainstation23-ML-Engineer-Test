import mysql.connector

cnx = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    port='3306',
    database='online_retail_data_set'
)

def get_most_order_countrywise():
    query = "SELECT Country FROM online_retail_data_set.customers GROUP BY Country ORDER BY COUNT(*) DESC LIMIT 1;"
    
    cursor = cnx.cursor()
    # Executing the SQL query to get the total order price
    cursor.execute(query)

    # Fetching the result
    result = cursor.fetchone()[0]

    # Closing the cursor
    cursor.close()

    return result
