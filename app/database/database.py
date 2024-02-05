import psycopg2
import os
from app.vitalina_utilities.utilities import bcolors

db_config = {
    'host': os.getenv("DB_HOST"),
    'database': os.getenv("DB_DATABASE"),
    'user': os.getenv("DB_USERNAME"),
    'password': os.getenv("DB_PASSWORD"),
    'port': os.getenv("DB_PORT")
}

def dbInsert(query, values):
    try:
        # Establish a connection to the PostgreSQL database
        connection = psycopg2.connect(**db_config)

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Define the SQL query to insert a record into your table

        ### INSERT INTO your_table_name (column1, column2, column3) VALUES (%s, %s, %s)

        insert_query = query

        # Replace the placeholder values with the actual values you want to insert
        
        ### ('value1', 'value2', 'value3')
        
        record_to_insert = values

        cursor.execute(insert_query, record_to_insert)


        # Commit the changes if necessary
        connection.commit()

    except (Exception, psycopg2.Error) as error:
        print(bcolors.FAIL + "Error while connecting to PostgreSQL:" + error + bcolors.ENDC)

    finally:
        # Close the cursor and connection
        if connection:
            cursor.close()
            connection.close()
            print("Connection to PostgreSQL closed")

def dbSelect(query):
    try:
        # Establish a connection to the PostgreSQL database
        connection = psycopg2.connect(**db_config)

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Define the SQL query to insert a record into your table

        ### SELECT * FROM your_table_name ORDER BY random() LIMIT 1

        insert_query = query

        cursor.execute(insert_query)

        # Commit the changes if necessary
        connection.commit()

        # Fetch the result
        row = cursor.fetchone()

        return row

    except (Exception, psycopg2.Error) as error:
        print(bcolors.FAIL + "Error while connecting to PostgreSQL:" + error + bcolors.ENDC)

    finally:
        # Close the cursor and connection
        if connection:
            cursor.close()
            connection.close()
            print("Connection to PostgreSQL closed")

def selectRandomMessage():
    random_message = dbSelect("SELECT message FROM all_messages ORDER BY random() LIMIT 1")
    return random_message[0]