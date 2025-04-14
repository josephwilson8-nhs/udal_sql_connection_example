This is the python code you can use to connect to SQL Server in UDAL, query a table, and return the results as a pandas dataframe.

# Create your environment

After cloning the repo to UDAL (or copying the functions into your existing project), make sure you have a python environment set up. If not, run these commands in Bash:

```
python -m venv venv
source venv/Scripts/activate
```

# Install dependencies

Then you'll need to install a few packages, so run:

```
pip install -r requirements.txt
```

If you already have a requirements.txt file, pyproject.toml, or similar, check the requirements.txt of this repo, and add these packages to your existing file if they are not already there.

# Create the .env file

To avoid committing the server addresses and usernames, we add them to the .env file. If you're copying this code into an existing project, make sure the .env file is added to your .gitignore file. Make double sure!

Then create a file called .env and add the following to it:

```
server="replace this with the server"
uid="your.name@udal.nhs.uk"
database="replace this with the database name"
```

Make the necessary replacements, and then save the file. Note that there are no spaces around the equals signs.

# Connecting to the Server

The `make_connection()` function in src/data_imports/sql_server.py connects to SQL Server and returns a `conn` object. You use this to send your queries to SQL Server.

# Write/add your SQL query

Make a .sql file in /sql with your query in it. 

# Run the query and return results as a Pandas dataframe

Call `get_df_from_sql_query()` in src/data_imports/sql_server.py and pass your `conn` object and the path to your query. This function will run your query on the server and return the results into a Pandas DataFrame. 

Alternatively, you can pass a db, schema, and tablename, and the function will `select *` from that table. Then you can manipulate the data with Pandas. But note that the SQL Server is likely much beefier than your VM compute-wise, so if it's a big table, it'll probably be faster to do the heavy lifting on the server.
