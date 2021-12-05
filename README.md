# robot



Step 1: 
pip install -r requirements.txt

Step 2:
change below variables in config.py in Config folder 
self.host=< > 
self.database_name=< > 
self.user= < > 
self.password= < >

step 3:
python app.py

Step 4:
End point to insert data in to db


method = post ########
http://127.0.0.1:9901/insert

Payload ############

please change id key in payload for each request

{"id": 41, "Robot_number": "5", "Room_number": "2", "Total_disinfection": 2.7, "Start_date_time": 3.3, "End_date_time": 3.42, "Normal_or_power": 1, "Start_battery_percent": 1, "End_battery_percent": 1, "Customer_name": "satish", "Disinfection_type": "normal",
  "Disinfection_Map": "imagebyte"}

Step 5:
Endpoint to get data from db ####
Method=Get #######
http://127.0.0.1:9901/getdata

Endpoint to get data from db page wise 
####please change page number to get data for each page and default page number is 1 

http://127.0.0.1:9901/getdata?page=2


Get total data from db

http://127.0.0.1:9901/total_data

End point for filterd_data with column_name and given value 

---------------------------------------------------------------
filter_column = give your column name to be search 

value = give you value to be search in given column name

http://127.0.0.1:9901/filter_data?filter_column=Room_number&value=4



