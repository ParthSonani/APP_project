import json
import pandas as pd
import sqlite3

conn = sqlite3.connect('flight.db')

cursor = conn.cursor()

f = open('data.json')
data = json.load(f)
print(data)

cursor.executescript('''drop table if exists flight_detail; drop table if exists departure; drop table if exists arrival;
create table flight_detail (id integer PRIMARY KEY AUTOINCREMENT, flight_date varchar,flight_status varchar, departure_id int,arrival_id int);
create table departure (departure_id integer PRIMARY KEY AUTOINCREMENT, airport varchar, timezone varchar, gate varchar, terminal varchar);
create table arrival (arrival_id integer PRIMARY KEY AUTOINCREMENT, airport varchar, timezone varchar, gate varchar, terminal varchar)''')

for i in range(len(data)):
    airportd = data[i]['departure']['airport']
    timezoned = data[i]['departure']['timezone']
    gated = data[i]['departure']['gate']
    terminald = data[i]['departure']['terminal']
    cursor.execute('''insert into departure (airport,timezone,gate,terminal) values (?,?,?,?)''',(airportd,timezoned,gated,terminald))
    airporta = data[i]['arrival']['airport']
    timezonea = data[i]['arrival']['timezone']
    gatea = data[i]['arrival']['gate']
    terminala = data[i]['arrival']['terminal']
    cursor.execute('''insert into arrival (airport,timezone,gate,terminal) values (?,?,?,?)''',
                   (airporta, timezonea, gatea, terminala))
    flight_date = data[i]['flight_date']
    flight_status = data[i]['flight_status']
    flight_name = data[i]['airline']['name']
    dep_id ='''select departure_id from departure where airport = (?)'''
    cursor.execute(dep_id,airportd)
    d_id = cursor.fetchall()
    print(d_id)
    cursor.execute('''insert into flight_detail (airport,timezone,gate,terminal) values (?,?,?,?)''',
                   (airporta, timezonea, gatea, terminala))
    conn.commit()

cursor.close()
conn.close()




