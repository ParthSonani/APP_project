
import json
from TDG import TableDataGateway

TableDataGateway = TableDataGateway()


def table_creation():
    f = open('data.json')
    data = json.load(f)
    TableDataGateway.create_tables()
    TableDataGateway.insert_data_departure(data)
    TableDataGateway.insert_data_arrival(data)
    TableDataGateway.insert_data_flight_detail(data)


def display_operations(table_n):
    table_name = table_n
    print("\nChoose operation to perform on " + table_name + " :\n 1. Update\n 2. Delete \n 3. Download table (.csv)\n"
                                                             " 4. Search \n 5. Press 0 to exit")


def get_input():
    table_name = input("\nEnter the name of table you wish to access (Press 0 to exit): ")

    return table_name

table_creation()

while True:
    print("\n---- Table list ----")
    tables = TableDataGateway.sql_fetch()
    table_name = get_input()

    if (table_name in tables):

        # Display table and return list of column names
        col_name = TableDataGateway.display_tables(table_name)

        display_operations(table_name)
        op = input("Input here: ")

        # Update query
        if (op == "1" or op == "update" or op == "Update"):
            TableDataGateway.update_data(col_name, table_name)

        # Delete query
        if (op == "2" or op == "delete" or op == "Delete"):
            TableDataGateway.delete_data(col_name, table_name)

        # Download data
        if (op == "3" or op == "download" or op == "Download table"):
            TableDataGateway.download_data(table_name)

        # Search data
        if (op == "4" or op == "search" or op == "Search"):
            TableDataGateway.search_data(table_name)

        # Exit application
        if (op == "0" or op == "4" or op == "exit"):
            None

    else :
        exit()

