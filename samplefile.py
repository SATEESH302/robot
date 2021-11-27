import mysql.connector

import mysql.connector
from mysql.connector import Error
# to connect db
connection = mysql.connector.connect(host='localhost',
                                         database='student',
                                         user='root',
                                         password='sat@12345')
#to create robot table

mySql_Create_Table_Query = """CREATE TABLE samrobot (
                         Id int(11) NOT NULL,
                         Robot_number varchar(250) NOT NULL,
                         Room_number varchar(20) NOT NULL,
                         Total_disinfection  float NOT NULL,
                         Start_date_time  float NOT NULL,
                         End_date_time  float NOT NULL,
                         Normal_or_power int(11) NOT NULL,
                         Start_battery_percent int(11) NOT NULL,
                         End_battery_percent int(11) NOT NULL,
                         Customer_name varchar(250) NOT NULL,
                         Disinfection_type varchar(250) NOT NULL,
                         PRIMARY KEY (Id)) """

cursor = connection.cursor()
result = cursor.execute(mySql_Create_Table_Query)
print("SAMROBOT Table created successfully ")

# __________________
#To Insert data in to db samrobot
# mySql_insert_query = """INSERT INTO samrobot (Id,Robot_number, Room_number, Total_disinfection,
#                          Start_date_time,End_date_time,Normal_or_power,Start_battery_percent,
#                          End_battery_percent,Customer_name,Disinfection_type)
#                            VALUES
#                            (6,'5','2','2.7','3.40','3.42',1,1,1,'satish','normal')
#                              """
# cursor = connection.cursor()
# cursor.execute(mySql_insert_query)
# connection.commit()
# print(cursor.rowcount, "Record inserted successfully into Laptop table")
# cursor.close()

# sql_select_Query = "select * from samrobot"
# cursor = connection.cursor()
# cursor.execute(sql_select_Query)
# # get all records
# records = cursor.fetchall()
# print("Total number of rows in table: ", cursor.rowcount)
# #
# # print("\nPrinting each row")
# for row in records:
#     print(row)



d={'id':13 , 'Robot_number':'5' , 'Room_number':'2' , 'Total_disinfection':3.7 ,'Start_date_time':4.3,
   'End_date_time':3.42 , "Normal_or_power":1 ,'Start_battery_percent':1 , 'End_battery_percent':1 ,
   'Customer_name':'satish','Disinfection_type':'normal'}
#
#
#
#
# mySql_insert_query = """INSERT INTO samrobot (Id,Robot_number, Room_number, Total_disinfection,
#                          Start_date_time,End_date_time,Normal_or_power,Start_battery_percent,
#                          End_battery_percent,Customer_name,Disinfection_type)
#                            VALUES
#                            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """
#
# cursor = connection.cursor()
# cursor.execute(mySql_insert_query,(d['id'],str(d['Robot_number']),str(d['Room_number']),\
#                                    str(d['Total_disinfection']),\
#                                     str(d['Start_date_time']),str(d['End_date_time']),\
#                                     d['Normal_or_power'],d['Start_battery_percent'],\
#                                      d['End_battery_percent'],str(d['Customer_name']),\
#                                     str(d['Disinfection_type'])))
# connection.commit()
# print(cursor.rowcount, "Record inserted successfully into Laptop table")
# cursor.close()




# data1={'data':[]}
# data1['data'].append(d)
# import json
# with open('data.json', 'w') as f:
#     json.dump(data1, f)

cursor = connection.cursor()

# page=1
# perpage = 20
# startat = page * perpage
# cursor.execute("select * from samrobot limit %s, %s",(0,3))


# def fetch_data_from_db(self, page):
#     mySql_insert_query = "select * from samrobot"
#     cursor.execute("select * from samrobot limit , 10")
#     cursor = self.dbconnection.cursor()
#     cursor.execute(mySql_insert_query)
#     # fetching all records from database
#     data = cursor.fetchall()
#     print(data)
#     return data

# fetching all records from database
# data = cursor.fetchall()
# print(data)
#
#
# list_of_columns=['id', 'Robot_number',\
#    'Room_number', 'Total_disinfection', \
#     'Start_date_time', 'End_date_time', \
#    'Normal_or_power', 'Start_battery_percent', \
#    'End_battery_percent', 'Customer_name',\
#    'Disinfection_type']

# print(c)
# total={'data': [(1, '5', '2', 2.7, 3.4, 3.42, 1, 1, 1, 'satish', 'normal'), (2, '5', '2', 2.7, 3.4, 3.42, 1, 1, 1, 'satish', 'normal'), (3, '5', '2', 2.7, 3.4, 3.42, 1, 1, 1, 'satish', 'normal'), (4, '5', '2', 2.7, 3.4, 3.42, 1, 1, 1, 'satish', 'normal'), (5, '5', '2', 2.7, 3.4, 3.42, 1, 1, 1, 'satish', 'normal'), (6, '5', '2', 2.7, 3.4, 3.42, 1, 1, 1, 'satish', 'normal'), (12, '5', '2', 3.7, 4.3, 3.42, 1, 1, 1, 'satish', 'normal'), (13, '5', '2', 3.7, 4.3, 3.42, 1, 1, 1, 'satish', 'normal'), (14, '5', '2', 2.7, 3.3, 3.42, 1, 1, 1, 'satish', 'normal'), (15, '5', '2', 2.7, 3.3, 3.42, 1, 1, 1, 'satish', 'normal'), (16, '5', '2', 2.7, 3.3, 3.42, 1, 1, 1, 'satish', 'normal'), (17, '5', '2', 2.7, 3.3, 3.42, 1, 1, 1, 'satish', 'normal'), (18, '5', '2', 2.7, 3.3, 3.42, 1, 1, 1, 'satish', 'normal'), (19, '5', '2', 2.7, 3.3, 3.42, 1, 1, 1, 'satish', 'normal'), (20, '5', '2', 2.7, 3.3, 3.42, 1, 1, 1, 'satish', 'normal'), (21, '5', '2', 2.7, 3.3, 3.42, 1, 1, 1, 'satish', 'normal'), (22, '5', '2', 2.7, 3.3, 3.42, 1, 1, 1, 'satish', 'normal'), (23, '5', '2', 2.7, 3.3, 3.42, 1, 1, 1, 'satish', 'normal'), (24, '5', '2', 2.7, 3.3, 3.42, 1, 1, 1, 'satish', 'normal'), (31, '5', '2', 2.7, 3.3, 3.42, 1, 1, 1, 'satish', 'normal'), (32, '5', '2', 2.7, 3.3, 3.42, 1, 1, 1, 'satish', 'normal'), (33, '5', '2', 2.7, 3.3, 3.42, 1, 1, 1, 'satish', 'normal'), (34, '5', '2', 2.7, 3.3, 3.42, 1, 1, 1, 'satish', 'normal'), (35, '5', '2', 2.7, 3.3, 3.42, 1, 1, 1, 'satish', 'normal'), (36, '5', '2', 2.7, 3.3, 3.42, 1, 1, 1, 'satish', 'normal'), (37, '5', '2', 2.7, 3.3, 3.42, 1, 1, 1, 'satish', 'normal'), (38, '5', '2', 2.7, 3.3, 3.42, 1, 1, 1, 'satish', 'normal'), (39, '5', '2', 2.7, 3.3, 3.42, 1, 1, 1, 'satish', 'normal'), (40, '5', '2', 2.7, 3.3, 3.42, 1, 1, 1, 'satish', 'normal'), (41, '5', '2', 2.7, 3.3, 3.42, 1, 1, 1, 'satish', 'normal')]}
# datafinal=[]
# for i in total['data']:
#     records={}
#     for k in range(len(i)):
#         records[c[k]]=i[k]
#     datafinal.append(records)
# print(len(datafinal))








