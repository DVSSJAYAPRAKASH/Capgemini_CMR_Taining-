import pymysql

def connect_db():
    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='123456',
            database='department',
           # cursorclass=pymysql.cursors.DictCursor
        )
        print('MySQL connected successfully')
        return connection
    except pymysql.MySQLError as err:
        print(f"Something went wrong: {err}")
        return None

def create_table(connection):
    with connection.cursor() as cursor:
        try:
            query = """CREATE TABLE IF NOT EXISTS EMPLOYEE (
                        id INT AUTO_INCREMENT PRIMARY KEY, 
                        name VARCHAR(255), 
                        age INT, 
                        salary INT
                    );"""
            cursor.execute(query)
            print('Table created successfully')
        except pymysql.MySQLError as err:
            print(f"Something went wrong: {err}")

def inserting_data(connection):
    with connection.cursor() as cursor:
        try:
            query = """INSERT INTO EMPLOYEE(name, age, salary) VALUES (%s, %s, %s)"""
            n = int(input("Enter the number of records to insert: "))
            data = [(input("Enter name: "), int(input("Enter age: ")), int(input("Enter salary: "))) for _ in range(n)]
            cursor.executemany(query, data)
            connection.commit()
            print('Data inserted successfully')
        except pymysql.MySQLError as err:
            print(f"Something went wrong: {err}")

def select_all_data(connection):
    with connection.cursor() as cursor:
        try:
            query = """SELECT * FROM EMPLOYEE;"""
            cursor.execute(query)
            result = cursor.fetchall()
            for row in result:
                print(row)
        except pymysql.MySQLError as err:
            print(f"Something went wrong: {err}")

def updating_data(connection):
    with connection.cursor() as cursor:
        try:
            query = """UPDATE EMPLOYEE SET salary = 7000 WHERE name = 'shanmuk';"""
            cursor.execute(query)
            connection.commit()
            print('Data updated successfully')
        except pymysql.MySQLError as err:
            print(f"Something went wrong: {err}")

def deleting_data(connection):
    with connection.cursor() as cursor:
        try:
            query = """DELETE FROM EMPLOYEE WHERE id = 1;"""
            cursor.execute(query)
            connection.commit()
            print('Data deleted successfully')
        except pymysql.MySQLError as err:
            print(f"Something went wrong: {err}")

def sort_data(connection):
    with connection.cursor() as cursor:
        try:
            query = """SELECT * FROM EMPLOYEE ORDER BY salary DESC;"""
            cursor.execute(query)
            result = cursor.fetchall()
            for row in result:
                print(row)
        except pymysql.MySQLError as err:
            print(f"Something went wrong: {err}")

def query_with_filter(connection):
    with connection.cursor() as cursor:
        try:
            query = """SELECT * FROM EMPLOYEE WHERE salary > %s;"""
            cursor.execute(query, (5000,))
            result = cursor.fetchall()
            for row in result:
                print(row)
        except pymysql.MySQLError as err:
            print(f"Something went wrong: {err}")

def drop_table(connection):
    with connection.cursor() as cursor:
        try:
            query = """DROP TABLE IF EXISTS EMPLOYEE;"""
            cursor.execute(query)
            connection.commit()
            print('Table dropped successfully')
        except pymysql.MySQLError as err:
            print(f"Something went wrong: {err}")

def drop_database(connection):
    with connection.cursor() as cursor:
        try:
            query = """DROP DATABASE IF EXISTS department;"""
            cursor.execute(query)
            connection.commit()
            print('Database dropped successfully')
        except pymysql.MySQLError as err:
            print(f"Something went wrong: {err}")

def main():
    connection = connect_db()
    if not connection:
        return

    # Uncomment the functions as needed:
    create_table(connection)
    inserting_data(connection)
   # updating_data(connection)
   # deleting_data(connection)
   # sort_data(connection)
   # query_with_filter(connection)
    #drop_table(connection)
    #select_all_data(connection)
    #drop_database(connection)

    connection.close()
    print('MySQL connection closed')

if __name__ == "__main__":
    main()
