import psycopg2
import json

# Above is a module used to interact with postgres
# Also, json is used to seralize objects to json

conn_params = {
    "dbname": "excercise_db",
    "user": "postgres",
    "password": "Abdul7293%",
    "host": "localhost",
    "port": 5432,
}


# Above is a dictionary object that holds ur connection properties.

conn = None

#  initally set connection as none

try:
    # Above same as try

    conn = psycopg2.connect(**conn_params)

    # Above makes our connection with psycopg2

    if conn:
        print("connection est")

    # Above, checks if our connection is establised.

    cursor = conn.cursor()

    # Above we create a cursor object from our connection
    # this allows us to query the db

    cursor.execute('SELECT * FROM "Exercise"')
    # Above we execute a query

    rows = cursor.fetchall()
    # Above we save the rows for that query
    # .fetch all helps gather results from previous query

    columns_workout = [desc[0] for desc in cursor.description]

    # Above is a example of list comprehension
    # It allows you to generate lists using a single line of code, typically
    # consisting of a loop and an optional condition.
    # This approach is often more readable and faster than
    # using traditional loops for creating lists.

    exercise_data = [dict(zip(columns_workout, row)) for row in rows]

    # Above we use list comprehension again
    # Above is converting the data in to dictionaries or objects by using the rows and columns
    # We itterate over the rows and use zip to align that columns properties with that rows values.
    # Last we use dict to turn that result into a dictionary or object.
    # List comprehension syntax is new_list = [expression for item in iterable if condition], the if condition is optional

    exercise_data_json = json.dumps(exercise_data, indent=4)

    # After assigning or key and value pairs with list comprehensions we convert the data to json.
    # .dumps from json allows us to do this
    # indent is the amount of space before next object

    print(exercise_data_json)

    # Above accesses our db and transforms the results to json


except Exception as e:
    # Above same as catch
    # Exception is used to as throw exception for error handle
    print(f"Error connecting to the database: {e}")
    # f is what allows us to use variables like  {e} in string


finally:
    # Above same a finally
    if conn:
        # Above check if connection exists
        cursor.close()
        conn.close()
        # Above close the connection and cursor if exists.
        print("connection closed")
