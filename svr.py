from flask import Flask
from flask import request, jsonify, render_template
from flask_cors import CORS, cross_origin
from crawl_stock_list_hn30_vn30 import get_top30
from crawl_stock_price import get_price_at_date
# Doan ma khoi tao server
app = Flask(__name__)
CORS(app)

# Khai bao ham xu ly request index
@app.route('/',methods=['GET'])
@cross_origin()
def index():
    return render_template('index.html')

@app.route('/update30',methods=['POST'])
@cross_origin()
def update30():
    for top_of_floor in ('HNX30', "VN30"):
        get_top30(top_of_floor)

    return render_template('index.html', msg= "Update HN30, VN30 thành công!")


@app.route('/crawl',methods=['POST'])
@cross_origin()
def crawl():
    datepick = request.form["datepick"]

    get_price_at_date(datepick)

    return render_template('index.html', msg= "Crawl giá ngày {} thành công!".format(datepick), file=datepick)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)