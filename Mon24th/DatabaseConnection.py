import pymysql as sql

try:
    # Create a connection to the database
    connection = sql.connect(host="localhost", port=3306, user="root", password="root", database="test")

    # Create a cursor object
    my_cursor = connection.cursor()

    # query = 'Insert into employee values (1001,"om",90000),(2001,"tim",75000)'
    query= 'delete from employee where emp_id = 1001'
    query = 'select * from employee'
    # my_cursor.execute("Create table employee(emp_id int,name varchar(30), salary int)")
    my_cursor.execute(query)

    # fetch using fetech all
    # data=my_cursor.fetchall()
    # print(data)

    #fetch using fetchone
    data1=[]
    data1.append(my_cursor.fetchone())
    data1.append( my_cursor.fetchone())
    data1.append(my_cursor.fetchone())
    print(data1)


    # Commit the database
    connection.commit()

    # Close cursor and connection
    my_cursor.close()
    connection.close()

except Exception as e:
    print(e)
