import sqlite3
import json
from connection1 import Connection
import pandas as pd
from TDG import TableDataGateway

TableDataGateway = TableDataGateway()

def table_creation():
    f = open('data.json')
    data = json.load(f)
    print(data)
    TableDataGateway.create_tables()
    TableDataGateway.insert_data_departure(data)
    TableDataGateway.insert_data_arrival(data)
    TableDataGateway.insert_data_flight_detail(data)

def display_operations(table_n):
    table_name = table_n
    print("\nChoose operation to perform on " + table_name + " :\n 1. Update\n 2. Delete \n 3. Download table (.csv)\n"
                                                             " 4. Enter to 0 to exit \n")

def get_input():
    table_name = input("\n\nEnter the name of table you wish to access (Press 0 to exit): ")

    return table_name

table_creation()

while True:
    tables = TableDataGateway.sql_fetch()
    table_name = get_input()

    if (table_name in tables):

        # Display table and return list of column names
        col_name = TableDataGateway.display_tables(table_name)

        display_operations(table_name)
        op = input("Input here: ")

        # Update query
        if (op == "1" or op == "update" or op == "Update"):
            # print("hahahah")
            # update_id = input("Enter "+col_name[0]+ " of the record to be updated : ")
            #id = col_name[0]
            TableDataGateway.update_data(col_name, table_name)

        # Delete query
        if (op == "2" or op == "delete" or op == "Delete"):
            # delete_id = input("Enter " + col_name[0] + " of the record to be deleted : ")
            #id = col_name[0]
            TableDataGateway.delete_data(col_name, table_name)

        # Download data
        if (op == "3" or op == "download" or op == "Download table"):
            TableDataGateway.download_data(table_name)

        # Exit application
        if (op == "0" or op == "4" or op == "exit"):
            exit()

    else :
        exit()

