import sqlite3
import json
import pandas as pd

def convertTuple(tup):
    str = ''.join(tup)
    return str

def sql_fetch(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT name from sqlite_master where type= "table"')
    table_l = cursorObj.fetchall()
    table_list = []
    for i in table_l:
        j = convertTuple(i)
        table_list.append(j)
        print(j)

    return table_list

def display_tables(tb_name):
    table_name = tb_name

    if (table_name == i):
        cursor.execute(('SELECT * FROM "{}" '.format(table_name.replace('"', '""'))))
        tab = cursor.fetchall()
        col_name = [i[0] for i in cursor.description]
        col_len = len(col_name)
        # for a in col_name:
        print("--------------------------------------------------------------------")
        print(*col_name, sep=" | ")
        print("--------------------------------------------------------------------")
        stmt = []
        for row in tab:
            print(row)
            # print(str(row[0]),'  |  ', str(row[1]), '|', str(row[2]), '|', str(row[3]), '|', str(row[4]))

        display_operations()
        op = input("Input here: ")

        # Update query
        if (op == "1" or op == "update" or op == "Update"):
            # print("hahahah")
            # update_id = input("Enter "+col_name[0]+ " of the record to be updated : ")
            id = col_name[0]
            update_data(id, col_name)

        # Delete query
        if (op == "2" or op == "delete" or op == "Delete"):
            # delete_id = input("Enter " + col_name[0] + " of the record to be deleted : ")
            id = col_name[0]
            delete_data(id, col_name)

        # Download data
        if (op == "3" or op == "download" or op == "Download table"):
            download_data()

        # Exit application
        if (op == "0" or op == "4" or op == "exit"):
            exit()


def display_operations():
    print("\nChoose operation to perform on " + table_name + " :\n 1. Update\n 2. Delete \n 3. Download table (.csv)\n"
                                                             " 4. Enter to 0 to exit \n")

def update_data(col, col_name):
    update_id = input("Enter " + col_name[0] + " of the record to be updated : ")
    id = col
    try:
        # print(table_name)
        rec = cursor.execute(('SELECT * FROM ' + table_name + ' WHERE "{}"=?'.format(id.replace('"', '""'))),
                             (update_id,))
        rec = rec.fetchone()
        print(rec)
        print("\nChoose record to update: ")
        for cols in col_name[1:]:
            print(cols)

        up_no = input("\n Input here: ")

        for cols in col_name[1:]:
            if (up_no == cols):
                up_rec = input("\n Enter the updated value : ")
                rec1 = cursor.execute('UPDATE ' + table_name + ' SET ' + cols + '=? WHERE ' + id + '=' + update_id + '',
                                      (up_rec,))
                rec1 = rec1.rowcount
                print("\nNumber of rows affected: " + str(rec1))
                conn.commit()
                print("Record updated successfully !!!\n")
                rec2 = cursor.execute(('SELECT * FROM ' + table_name + ' WHERE "{}"=?'.format(id.replace('"', '""'))),
                                      (update_id,))
                rec2 = rec2.fetchone()
                print(rec2)


    except Exception as e:
        print(e)

def delete_data(col, col_name):
    id = col
    delete_id = input("Enter " + col_name[0] + " of the record to be deleted : ")
    try:

        rec = cursor.execute(('SELECT * FROM ' + table_name + ' WHERE "{}"=?'.format(id.replace('"', '""'))),
                             (delete_id,))
        rec = rec.fetchone()
        print(rec)
        ans = input("\nAre you sure you want to delete this record? (Y/n): ")

        if (ans == 'Y' or ans == 'y'):
            rec1 = cursor.execute('DELETE from ' + table_name + ' WHERE ' + id + '=' + delete_id + '')
            rec1 = rec1.rowcount
            print("\nNumber of rows affected: " + str(rec1))
            conn.commit()
            print("Record deleted successfully !!!\n")

    except Exception as e:
        print(e)

def download_data():
    db_df = pd.read_sql_query('SELECT * FROM ' + table_name + '', conn)
    db_df.to_csv('' + table_name + '.csv', index=False)
    print("Records for table " + table_name + " downloaded successfully !!!")



# Database connection
print("Connecting to local database ...")
conn = sqlite3.connect('flight.db')
cursor = conn.cursor()
print("Connected to flight database !!")
print("List of tables:-")

tables = sql_fetch(conn)

table_name = input("Enter the name of table you wish to access: ")

for i in tables:
    display_tables(table_name)
