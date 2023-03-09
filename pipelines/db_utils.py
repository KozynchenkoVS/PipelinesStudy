import sqlite3,csv, re
from sqlite3 import Error

def domain_of_url(url):
    return re.search("((?<=http:\/\/)|(?<=https:\/\/)).+?(?=\/)", str(url)).group(0)

def execute_query( query : str, connection_string : str):
    connection_to_db = sqlite3.connect(connection_string)
    try:
        connection_to_db.execute(query)
        connection_to_db.commit()
        connection_to_db.close()
    except Error as err:
        print("|ERROR|", err)

def create_table_as(table : str, query : str, connection_string : str):
    connection_to_db = sqlite3.connect(connection_string)
    connection_to_db.create_function("domain_of_url", 1, domain_of_url)
    try:
        connection_to_db.execute("create table if not exists " + table + " AS " + query)
        connection_to_db.commit()
        connection_to_db.close()
    except Error as err:
        print("|ERROR|", err)

def load_file_to_table(filename : str, table : str, connection_string : str):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        fields = determine_fields(next(reader))
        create_query = 'create table if not exists ' + table + ' (' + ','.join(f'{key} {value}' for key, value in fields.items()) + ');'
        execute_query(create_query, connection_string)
        for row in list(reader):
            for i in range(1,len(row)):
                row[i] = "'{}'".format(row[i])
            insert_query = 'INSERT INTO ' + table + '(' + ','.join(fields.keys()) + ') values(' + ','.join(row) + ');'
            execute_query(insert_query, connection_string)

def export_to_file_from_table(filename : str, table : str, connection_string : str):
    with open(f"{filename}.csv", "w") as file:
        cur = sqlite3.connect(connection_string).cursor()
        writer = csv.writer(file)
        writer.writerow(['id','name','url','domain_of_url'])
        data =  cur.execute("SELECT * FROM " + table)
        writer.writerows(data)
        cur.close()

def determine_fields(fields):
    """"Determining type of fields which was passed by file"""
    field_types = {}
    for field in fields:
        if field == 'id':
            field_types[field] = "integer PRIMARY KEY"
        else: field_types[field] = "text NOT NULL"
    return field_types