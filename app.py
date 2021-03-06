from flask import *
from db_modules.db_table import table
from utils import *
from flask_cors import CORS,cross_origin

app = Flask(__name__)

CORS(app,allow_headers='*',)
app.config['CORS_HEADERS']='content_type'
data_table = table()


@app.route('/insert', methods=['POST'])
@cross_origin()
def insert_data():
    if request.method == 'POST':

        try:
            d = request.get_json()
            msg = data_table.insert_data(d)
            results = {'message': msg}
            response = jsonify(results)
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
        except Exception as e:
            results = {"error": str(e)}
            response = jsonify(results)
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response


@app.route('/getdata', defaults={'page': 1}, methods=['POST', 'GET'])
@app.route('/getdata/page/<int:page>', methods=['POST', "GET"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def get_data_from_db(page):
    page = request.args.get('page')
    room_no = request.args.get('room')
    print(room_no)
    if request.method == 'GET' or request.method == 'POST':
        if page is None:
            page = int(1)
        alldata = data_table.fetch_data_from_db(page)
        response = jsonify(alldata)
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers["Content-Type"]='application/json'
        return response


@app.route('/total_data', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def get_total_data_db():
    print('content type',request.content_type)
    request.content_type='application/json'
    if request.method == 'GET':
        data = data_table.get_total_data()
        response = jsonify(data)
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response


@app.route('/filter_data', methods=['GET','POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def filter_data():

    print('content type',dict(request.headers))

    if request.method == 'GET':
        filter_value = request.args.get('filter_column')
        value = request.args.get('value')
        data = data_table.filter_data(filter_value, value)
        response = jsonify(data)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


if __name__ == '__main__':
    app.run(port=9901, debug=True)
