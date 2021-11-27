

list_of_columns=['id', 'Robot_number',\
   'Room_number', 'Total_disinfection', \
    'Start_date_time', 'End_date_time', \
   'Normal_or_power', 'Start_battery_percent', \
   'End_battery_percent', 'Customer_name',\
   'Disinfection_type']

def list_to_json(total):
    datafinal = []
    for i in total['data']:
        records = {}
        for k in range(len(i)):
            records[list_of_columns[k]] = i[k]
        datafinal.append(records)
    print(datafinal)
    return datafinal


