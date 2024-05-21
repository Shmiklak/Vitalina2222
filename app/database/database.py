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
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()
        ### INSERT INTO your_table_name (column1, column2, column3) VALUES (%s, %s, %s)

        insert_query = query

        ### ('value1', 'value2', 'value3')
        
        record_to_insert = values

        cursor.execute(insert_query, record_to_insert)
        connection.commit()

    except (Exception, psycopg2.Error) as error:
        print(bcolors.FAIL + "Error while connecting to PostgreSQL:" + error + bcolors.ENDC)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Connection to PostgreSQL closed")

def dbUpdate(query):
    try:
        # Establish a connection to the PostgreSQL database
        connection = psycopg2.connect(**db_config)

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Define the SQL query to insert a record into your table

        ### INSERT INTO your_table_name (column1, column2, column3) VALUES (%s, %s, %s)

        update_query = query
        cursor.execute(update_query)
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

def saveUser(discord_id, osu_user):
    user = dbSelect(f"SELECT * FROM osu_users WHERE discord_id={discord_id}")
    if (user == None):
        dbInsert("INSERT INTO osu_users (discord_id, osu_id) VALUES (%s, %s)", [discord_id, osu_user])
    else:
        dbUpdate(f"UPDATE osu_users SET osu_id={osu_user} WHERE discord_id={discord_id}")

def getUser(discord_id):
    user = dbSelect(f"SELECT osu_id FROM osu_users WHERE discord_id={discord_id}")
    if user == None:
        return "ERROR"
    return user[0]