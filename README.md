# SOEN6441_project
The system flow is as follows:
terminalui.py ---> TDG.py ---> connection.py

For refreshed data, run mainprog.py. It will pull new data from api and store it in a json file.

terminalui.py -- Interact with user providing list of tables available on database and the opertions that can be performed on individual tables.

TDG.py -- Interacts directly with the database. It runs parameterized queries on the database without allowing the terminalui.py to have direct access to the database.

connection.py -- Establishes the connection with the local database. Creates a single instance of the connection which the rest of the system uses.
