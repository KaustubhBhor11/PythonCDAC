import pymysql as sql


def connect_to_db(host='localhost', port=3306, user='root', password='root', database='test'):
    connection = sql.connect(host=host, port=port, user=user, password=password, database=database)

    return connection


def create_table(my_cursor, table_name, column_names):
    column_names_string = ""
    for i in column_names:
        column_names_string += f"{i[0]} {i[1]},"
    column_names_string = column_names_string[:-1]
    query = f'create table {table_name}({column_names_string})'
    my_cursor.execute(query)


def select_table(my_cursor, table_name, column_name="*", ):
    query = f"select {column_name} from {table_name}"
    my_cursor.execute(query)


connection = connect_to_db()
my_cursor = connection.cursor()

column_names = [["emp_id", "int"], ["name", "varchar(30)"], ["salary", "int"]]
create_table(my_cursor, 'test', column_names)
