import sqlite3
import json

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

# Database connection
print("Connecting to local database ...")
conn = sqlite3.connect('flight.db')
cursor = conn.cursor()
print("Connected to flight database !!")
print("List of tables:-")

tables = sql_fetch(conn)

table_name = input("Enter the name of table you wish to access: ")

for i in tables:
    if(table_name == i):
        cursor.execute(('SELECT * FROM "{}" '.format(table_name.replace('"', '""'))))
        tab = cursor.fetchall()
        col_name = [i[0] for i in cursor.description]
        #for a in col_name:
        print("--------------------------------------------------------------------")
        print(*col_name, sep = " | ")
        print("--------------------------------------------------------------------")

        for row in tab:
            #print(row.keys(0), row.keys(1), row.keys(2), row.keys(3), row.keys(4))
            print(str(row[0]),'  |  ', str(row[1]), '|', str(row[2]), '|', str(row[3]), '|', str(row[4]))

        print("\nChoose operation to perform on "+ table_name+" :\n 1. Update\n 2. Delete \n 3. Download table (.csv)\n"
                                                                 " 4. Enter to 0 to exit \n")
        op = input("Input here: ")
        if(op == "1" or op == "update" or op == "Update"):
            #print("hahahah")
            update_id = input("Enter "+col_name[0]+ " of the record to be updated : ")
            id = col_name[0]


            try:
                #print(table_name)
                rec = cursor.execute(('SELECT * FROM '+table_name+' WHERE "{}"=?'.format(id.replace('"', '""'))), (update_id,) )
                rec = rec.fetchone()
                print(rec)
                print("\nChoose record to update: ")
                for cols in col_name[1:]:
                    print(cols)

                up_no = input("\n Input here: ")

                for cols in col_name[1:]:
                    if(up_no == cols):
                        up_rec = input("\n Enter the updated value : ")
                        rec1 = cursor.execute('UPDATE '+table_name+' SET '+cols+'=? WHERE '+id+'='+update_id+'', (up_rec,))
                        rec1 = rec1.rowcount
                        print("\nNumber of rows affected: " +str(rec1))
                        conn.commit()
                        print("Record updated successfully !!!\n")
                        rec2 = cursor.execute(('SELECT * FROM '+table_name+' WHERE "{}"=?'.format(id.replace('"', '""'))), (update_id,))
                        rec2 = rec2.fetchone()
                        print(rec2)


            except Exception as e:
                print(e)

