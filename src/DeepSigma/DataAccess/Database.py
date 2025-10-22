import pandas as pd
import pyodbc
from typing import Type, List
from dataclasses import fields, is_dataclass


class Database:
    _server = ""
    _database = ""
    _connection_string = ""

    def __init__(self, server: str, database: str, username: str, password: str):
        self._server = server
        self._database = database
        self._connection_string = ("Driver={SQL Server Native Client 11.0};"
                                   + "Server=" + self._server + ";"
                                   + "Database=" + self._database + ";"
                                   + "uid=" + username + ";pwd=" + password + ";"
                                   + "Trusted_Connection=yes;")

    def get_data_in_dataframe(self, sql_query: str) -> pd.DataFrame:
        """
        Loads results of database query into pandas dataframe.
        :param sql_query:
        :return: DataFrame
        """
        connection = pyodbc.connect(self._connection_string)
        cursor = connection.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        df = pd.DataFrame(rows)
        connection.close()
        return df

    def load_objects(self, sql_query: str, class_to_load: Type) -> List[Type]:
        """
        Loads list of custom objects from the results of a database query.
        :param sql_query:
        :param class_to_load: Note: the class must be labeled @dataclass "from dataclasses import dataclass."
        :return: List[Objects]
        """
        connection = pyodbc.connect(self._connection_string)
        cursor = connection.cursor()
        cursor.execute(sql_query)

        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        results = Database._map_rows_to_objects(columns, rows, class_to_load)

        connection.close()
        return results

    @staticmethod
    def _map_rows_to_objects(columns, rows, model: Type) -> List:
        """
        Maps sql result rows to list of class object serialized with data.
        :param rows:
        :param model:
        :return: List[Objects]
        """
        if not is_dataclass(model):
            raise ValueError(f"{model} must be a dataclass type")

        model_fields = {field.name for field in fields(model)}
        return [model(**{k: v for k, v in zip(columns, row) if k in model_fields})
                for row in rows]
