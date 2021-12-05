import mysql.connector
from Config.config import db_config
import mysql.connector

class table():

    def __init__(self):
        self.db = db_config()
        self.dbconnection=self.sql_connection()
        pass

    def sql_connection(self):
        connection = mysql.connector.connect(host=self.db.host,
                                             database=self.db.database_name,
                                             user=self.db.user,
                                             password=self.db.password)
        return connection

    def  insert_data (self,d):

        mySql_insert_query = """INSERT INTO samrobot (Id,Robot_number, Room_number, Total_disinfection,
                                         Start_date_time,End_date_time,Normal_or_power,Start_battery_percent,
                                         End_battery_percent,Customer_name,Disinfection_type)
                                           VALUES
                                           (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """

        cursor = self.dbconnection.cursor()
        cursor.execute(mySql_insert_query, (d['id'], str(d['Robot_number']), str(d['Room_number']), \
                                            str(d['Total_disinfection']), \
                                            str(d['Start_date_time']), str(d['End_date_time']), \
                                            d['Normal_or_power'], d['Start_battery_percent'], \
                                            d['End_battery_percent'], str(d['Customer_name']), \
                                            str(d['Disinfection_type'])))
        self.dbconnection.commit()
        print(cursor.rowcount, "Record inserted successfully into samrobot table")
        cursor.close()
        return str(cursor.rowcount) +' ' + "Record inserted successfully into samrobot table"


    def fetch_data_from_db(self,page):
        mySql_insert_query="select * from samrobot limit %s,%s"
        perpage=5
        if page==1:
            cursor = self.dbconnection.cursor()
            cursor.execute(mySql_insert_query,(0,perpage))
            # fetching all records from database
            data = cursor.fetchall()
            total_data = {'data': []}
            for k in range(len(data)):
                records = []
                for j in range(len(data[k])):
                    records.append(data[k][j])
                total_data['data'].append(records)
            total_data['recordsTotal'] = len(total_data['data'])
            total_data['recordsFiltered'] = len(total_data['data'])
            print(total_data)
            return total_data
        else:
            page=int(page)-1
            startpage=page*5
            cursor = self.dbconnection.cursor()
            cursor.execute(mySql_insert_query,(startpage, perpage))
            # fetching all records from database
            data = cursor.fetchall()
            total_data = {'data': []}
            for k in range(len(data)):
                records = []
                for j in range(len(data[k])):
                    records.append(data[k][j])
                total_data['data'].append(records)
            total_data['recordsTotal'] = len(total_data['data'])
            total_data['recordsFiltered'] = len(total_data['data'])
            print(total_data)
            return total_data

    def get_total_data(self):
        mySql_insert_query = "select * from samrobot"
        cursor = self.dbconnection.cursor()
        cursor.execute(mySql_insert_query)
        # fetching all records from database
        data = cursor.fetchall()
        total_data = {'data': []}
        for k in range(len(data)):
            records = []
            for j in range(len(data[k])):
                records.append(data[k][j])
            total_data['data'].append(records)
        total_data['recordsTotal'] = len(total_data['data'])
        total_data['recordsFiltered'] = len(total_data['data'])

        print(total_data)
        return total_data