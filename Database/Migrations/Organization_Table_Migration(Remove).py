import mysql.connector

def create_organization_table():
    try:
        # Create a connection to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='Kit-Accounting-DB'
        )

        # Create a cursor to execute SQL queries
        cursor = connection.cursor()

        # Create the organization table
        table_name = 'organization'
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS {} (
            organization_id INT PRIMARY KEY AUTO_INCREMENT,
            user_id INT,
            email_address VARCHAR(255),
            phone_no VARCHAR(20),
            password VARCHAR(255),
            postal_address VARCHAR(255),
            physical_address VARCHAR(255),
            company_logo VARCHAR(255),
            FOREIGN KEY (user_id) REFERENCES user(user_id)
        )
        '''.format(table_name)

        cursor.execute(create_table_query)

        # Commit the changes
        connection.commit()
        print("Table 'organization' has been created successfully.")

    except mysql.connector.Error as error:
        print("Failed to create table in MySQL: {}".format(error))

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed.")

def delete_organization_table():
    try:
        # Create a connection to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='Kit-Accounting-DB'
        )

        # Create a cursor to execute SQL queries
        cursor = connection.cursor()

        # Delete the organization table
        table_name = 'organization'
        delete_table_query = '''
        DROP TABLE IF EXISTS {}
        '''.format(table_name)

        cursor.execute(delete_table_query)

        # Commit the changes
        connection.commit()
        print("Table 'organization' has been deleted successfully.")

    except mysql.connector.Error as error:
        print("Failed to delete table in MySQL: {}".format(error))

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed.")

# Call the function to create the organization table
create_organization_table()

# Call the function to delete the organization table
delete_organization_table()
