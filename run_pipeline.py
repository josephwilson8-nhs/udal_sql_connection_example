from src.data_imports import sql_server
import dotenv
import os

# load the secret information from the .env file
dotenv.load_dotenv(override=True)

# create the connection to SQL server
conn = sql_server.make_connection(os.environ["server"], os.environ["uid"], os.environ["database"])

# read a sql query from a file. You'll need to update this example with your own query.
example_query = sql_server.read_sql_query("./sql/select_top_1000.sql")

# run the query and return the results as a pandas dataframe
df_example = sql_server.get_df_from_sql_query(conn, query=example_query)

# display the data. 
print(df_example)

# OK you're on your own from here, good luck!
