import pyodbc
import pandas as pd
 
 
def make_connection(server, uid, database):
    """
    Connects to SQL Server using Windows Authentication
 
    Parameters:
    
    server (str): The name of the server you want to connect to

    returns:

    pyodbc connection object
    """
    conn_str = (
        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={server};'
        f'UID={uid};'
        f'DATABASE={database};'
        'Authentication=ActiveDirectoryInteractive;'
    )
    conn = pyodbc.connect(conn_str)
    
    return conn

def get_df_from_sql_query(conn, db="", schema="", table="", query=""):
    """
    Runs a SQL query on the SQL server, and returns the results as a pandas df.

    Parameters:

    conn (pyodbc connection object): Your server connection
    db (str): DB name
    schema (str): schema name
    table (str): table name
    query (str): query to run. If you pass a query, the function will ignore the above parameters and just run this query.
    If a query is not passed, it will default to select * from db.schema.table.
    
    Returns:

    pd.DataFrame: the results of the query as a pandas df.

    """
    if not query:
        query = f"""
            SELECT *
            FROM [{db}].[{schema}].[{table}]
        """
 
    df = pd.read_sql(query, conn)
 
    return df

def read_sql_query(path, replacements={}):
    """
    Reads a SQL query from a file and applies optional replacements.

    Parameters:
    path (str): The file path to the SQL query file.
    replacements (dict, optional): A dictionary where keys are placeholders in the SQL query
                                   and values are the replacements for those placeholders.

    Returns:
    str: The SQL query with replacements applied.
    """
    with open(path, 'r') as file:
        content = file.read()
        for replacement in replacements:
            content = content.replace(replacement, replacements[replacement])
    return content
