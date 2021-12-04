from flask import *
from db_modules.db_table import table
from utils import *

app = Flask(__name__)

data_table = table()


@app.route('/insert', methods=['POST'])
def insert_data():
    if request.method == 'POST':
        try:
            d = request.get_json()
            msg=data_table.insert_data(d)
            reutls={'message':msg}
            return reutls
        except Exception as e :
            reutls={"error":e}
            return reutls

@app.route('/getdata', defaults={'page':1})
@app.route('/getdata/page/<int:page>',methods=['POST','GET'])
def get_data_from_db(page):
    page=request.args.get('page')
    alldata = data_table.fetch_data_from_db(page)
    # total_records = {"data": alldata}
    # total_records={'datafinal':list_to_json(total_records)}
    return alldata

@app.route('/total_data', methods=['GET'])
def get_total_data_db():
    if request.method == 'GET':
        data = data_table.get_total_data()
        return data

if __name__ == '__main__':
    app.run(port=9901 , debug=True)