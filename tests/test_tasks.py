from pipelines.tasks import *
import os
import sqlite3
from sqlite3 import Error
import pytest

connection_string = 'test_table.db'
table = 'test_table'
file = 'tests/test_data.csv'
file_output = 'output'

def clean_up():
    RunSQL('drop table ' + table, db = connection_string).run()
    if os.path.isfile(file_output + '.csv'):
        os.remove(file_output + '.csv')
        os.remove(connection_string)

def test_task_load():
    task = LoadFile(table, file, db = connection_string)
    task.run()
    cursor = sqlite3.connect(connection_string).cursor()
    cursor.execute("SELECT COUNT(*) from " + table)
    actual_num_of_rows = cursor.fetchone()[0]
    assert actual_num_of_rows == 2
    clean_up()

def test_task_export():
    LoadFile(table, file, db = connection_string).run()
    CopyToFile(table, file_output, db = connection_string).run()
    if os.path.isfile(file_output + '.csv'):
        check_file = open(file_output + '.csv', 'r')
        reader = csv.reader(check_file)
        actual_num_of_rows = len(list(reader)) - 1
        assert actual_num_of_rows == 2
        clean_up()
    else: pytest.fail("File was not created")



