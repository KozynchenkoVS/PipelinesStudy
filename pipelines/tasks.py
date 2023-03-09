from pipelines.db_utils import *
class BaseTask:
    """Base Pipeline Task"""

    def run(self):
        raise RuntimeError('Do not run BaseTask!')

    def short_description(self):
        pass

    def __str__(self):
        task_type = self.__class__.__name__
        return f'{task_type}: {self.short_description()}'


class CopyToFile(BaseTask):
    """Copy table data to CSV file"""

    def __init__(self, table, output_file, db = 'test_database.db'):
        self.table = table
        self.output_file = output_file
        self.database = db

    def short_description(self):
        return f'{self.table} -> {self.output_file}'

    def run(self):
        print(f"Copy table `{self.table}` to file `{self.output_file}`")
        export_to_file_from_table(filename=self.output_file, table = self.table, connection_string= self.database)


class LoadFile(BaseTask):
    """Load file to table"""

    def __init__(self, table, input_file, db = 'test_database.db'):
        self.table = table
        self.input_file = input_file
        self.database = db
    def short_description(self):
        return f'{self.input_file} -> {self.table}'

    def run(self):
        print(f"Load file `{self.input_file}` to table `{self.table}`")
        load_file_to_table(filename=self.input_file, table= self.table, connection_string= self.database)

class RunSQL(BaseTask):
    """Run custom SQL query"""

    def __init__(self, sql_query, title=None, db = 'test_database.db'):
        self.title = title
        self.sql_query = sql_query
        self.database = db

    def short_description(self):
        return f'{self.title}'

    def run(self):
        print(f"Run SQL ({self.title}):\n{self.sql_query}")
        execute_query(self.sql_query, connection_string= self.database)



class CTAS(BaseTask):
    """SQL Create Table As Task"""

    def __init__(self, table, sql_query, title=None, db = 'test_database.db'):
        self.table = table
        self.sql_query = sql_query
        self.title = title or table
        self.database = db

    def short_description(self):
        return f'{self.title}'

    def run(self):
        print(f"Create table `{self.table}` as SELECT:\n{self.sql_query}")
        create_table_as(table=self.table, query=self.sql_query, connection_string= self.database)
