import sqlite3, pandas, csv, re
from sqlite3 import Error
connection_string = 'test_database.db'
def domain_of_url(url):
    return re.search("((?<=http:\/\/)|(?<=https:\/\/)).+?(?=\/)", str(url)).group(0)
def execute_query(query : str):
    connection_to_db = sqlite3.connect(connection_string)
    try:
        connection_to_db.execute(query)
        connection_to_db.commit()
    except Error as err:
        print("|ERROR|", err)
def create_table_as(table : str, query : str):
    connection_to_db = sqlite3.connect(connection_string)
    connection_to_db.create_function("domain_of_url", 1, domain_of_url)
    try:
        connection_to_db.execute("create table if not exists " + table + " AS " + query)
    except Error as err:
        print("|ERROR|", err)
def load_file_to_table(filename : str, table : str):
    connection_db = sqlite3.connect(connection_string)
    pandas.read_csv(f"{filename}").to_sql(name = table, con = connection_db, if_exists = 'append', index = False)
def export_to_file_from_table(filename : str, table : str):
    with open(f"{filename}.csv", "w") as file:
        cur = sqlite3.connect(connection_string).cursor()
        writer = csv.writer(file)
        writer.writerow(['id','name','url','domain_of_url'])
        data =  cur.execute("SELECT * FROM " + table)
        writer.writerows(data)