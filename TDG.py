import json
import sqlite3
import pandas as pd
from connection import Connection

class TableDataGateway:
    def __init__(self):
        c = Connection()
        conn = c.get_connection()
        self.conn = conn
        self.cursor = conn.cursor
        #print(self.cursor)

    def convertTuple(tup):
        str = ''.join(tup)
        return str

    def sql_fetch(self):
        #print(self.cursor)
        cursorObj = self.cursor()
        cursorObj.execute('SELECT name from sqlite_master where type= "table"')
        table_l = cursorObj.fetchall()
        table_list = []
        for i in table_l:
            j = TableDataGateway.convertTuple(i)
            table_list.append(j)
            print(j)

        return table_list

    def display_tables(self, table_name):
        #print(self.cursor)
        cursorObj = self.cursor()
        cursorObj.execute(('SELECT * FROM "{}" '.format(table_name.replace('"', '""'))))
        tab = cursorObj.fetchall()
        col_name = [i[0] for i in cursorObj.description]
        # col_len = len(col_name)
        # for a in col_name:
        print("--------------------------------------------------------------------")
        print(*col_name, sep=" | ")
        print("--------------------------------------------------------------------")
        for row in tab:
            print(row)
            # print(str(row[0]),'  |  ', str(row[1]), '|', str(row[2]), '|', str(row[3]), '|', str(row[4]))

        return col_name

    def update_data(self, col_name, table_name):
        update_id = input("Enter " + col_name[0] + " of the record to be updated : ")
        id = col_name[0]
        try:
            # print(table_name)
            cursorObj = self.cursor()
            conn = self.conn

            rec = cursorObj.execute(('SELECT * FROM ' + table_name + ' WHERE "{}"=?'.format(id.replace('"', '""'))),
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
                    rec1 = cursorObj.execute(
                        'UPDATE ' + table_name + ' SET ' + cols + '=? WHERE ' + id + '=' + update_id + '',
                        (up_rec,))
                    rec1 = rec1.rowcount
                    print("\nNumber of rows affected: " + str(rec1))
                    conn.commit()
                    print("Record updated successfully !!!\n")
                    rec2 = cursorObj.execute(
                        ('SELECT * FROM ' + table_name + ' WHERE "{}"=?'.format(id.replace('"', '""'))),
                        (update_id,))
                    rec2 = rec2.fetchone()
                    print(rec2)


        except Exception as e:
            print(e)

    def delete_data(self, col_name, table_name):
        id = col_name[0]
        delete_id = input("Enter " + col_name[0] + " of the record to be deleted : ")
        try:
            cursorObj = self.cursor()
            conn = self.conn

            rec = cursorObj.execute(('SELECT * FROM ' + table_name + ' WHERE "{}"=?'.format(id.replace('"', '""'))),
                                 (delete_id,))
            rec = rec.fetchone()
            print(rec)
            ans = input("\nAre you sure you want to delete this record? (Y/n): ")

            if (ans == 'Y' or ans == 'y'):
                rec1 = cursorObj.execute('DELETE from ' + table_name + ' WHERE ' + id + '=' + delete_id + '')
                rec1 = rec1.rowcount
                print("\nNumber of rows affected: " + str(rec1))
                conn.commit()
                print("Record deleted successfully !!!\n")

        except Exception as e:
            print(e)

    def download_data(self, table_name):
        db_df = pd.read_sql_query('SELECT * FROM ' + table_name + '', self.conn)
        db_df.to_csv('' + table_name + '.csv', index=False)
        print("Records for table " + table_name + " downloaded successfully !!!")

    def insert_data_departure(self, data):
        cursorObj = self.cursor()
        conn = self.conn
        for i in range(len(data)):
            airportd = data[i]['departure']['airport']
            timezoned = data[i]['departure']['timezone']
            gated = data[i]['departure']['gate']
            terminald = data[i]['departure']['terminal']
            cursorObj.execute('''insert into departure (airport,timezone,gate,terminal) values (?,?,?,?)''',
                           (airportd, timezoned, gated, terminald))
            conn.commit()
        print("Table departure records inserted succesfully !!!")

    def insert_data_arrival(self, data):
        cursorObj = self.cursor()
        conn = self.conn
        for i in range(len(data)):
            airporta = data[i]['departure']['airport']
            timezonea = data[i]['departure']['timezone']
            gatea = data[i]['departure']['gate']
            terminala = data[i]['departure']['terminal']
            cursorObj.execute('''insert into arrival (airport,timezone,gate,terminal) values (?,?,?,?)''',
                              (airporta, timezonea, gatea, terminala))
            conn.commit()
        print("Table arrival records inserted succesfully !!!")

    def insert_data_flight_detail(self, data):
        cursorObj = self.cursor()
        conn = self.conn
        for i in range(len(data)):
            flight_date = data[i]['flight_date']
            flight_status = data[i]['flight_status']
            flight_name = data[i]['airline']['name']
            airportd = data[i]['departure']['airport']
            airporta = data[i]['arrival']['airport']
            dep_id = '''select departure_id from departure where airport = (?)'''
            cursorObj.execute(dep_id, (airportd,))
            d_id = cursorObj.fetchone()
            #print('d:',d_id)
            arr_id = '''select arrival_id from arrival where airport = (?)'''
            cursorObj.execute(arr_id, (airporta,))
            a_id = cursorObj.fetchone()

            if(a_id == None or d_id == None):
                a_id = [1]
                d_id = [1]
                cursorObj.execute(
                    '''insert into flight_detail (flight_date,flight_status,airline_name,departure_id,arrival_id) values (?,?,?,?,?)''',
                    (flight_date, flight_status, flight_name, d_id[0], a_id[0]))
                conn.commit()
            else:
                cursorObj.execute(
                    '''insert into flight_detail (flight_date,flight_status,airline_name,departure_id,arrival_id) values (?,?,?,?,?)''',
                    (flight_date, flight_status, flight_name, d_id[0], a_id[0]))
                conn.commit()

        print("Table arrival records inserted succesfully !!!")

    def create_tables(self):
        cursorObj = self.cursor()
        cursorObj.executescript('''drop table if exists flight_detail; drop table if exists departure; drop table if exists arrival;
        create table flight_detail (id integer PRIMARY KEY AUTOINCREMENT, flight_date varchar,flight_status varchar,airline_name varchar, departure_id int,arrival_id int);
        create table departure (departure_id integer PRIMARY KEY AUTOINCREMENT, airport varchar, timezone varchar, gate varchar, terminal varchar);
        create table arrival (arrival_id integer PRIMARY KEY AUTOINCREMENT, airport varchar, timezone varchar, gate varchar, terminal varchar)''')
        print("Tables created succesfully !!!")