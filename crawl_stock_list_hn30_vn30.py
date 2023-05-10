import pandas as pd
import requests
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings

disable_warnings(InsecureRequestWarning)

def get_top30(top_of_floor):
    url = "https://mktapi1.mbs.com.vn/pbResfulMarkets/category/securities/list"
    myobj = '{"rid":"32423542","token":"","type":"SEC","code":"' + top_of_floor + '"}'
    Headers = {"Accept": "application/json, text/javascript, */*; q=0.01",
               "Accept-Encoding": "gzip, deflate, br",
               "Accept-Language": "en-US,en;q=0.9,vi;q=0.8",
               "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
               "Host": "mktapi1.mbs.com.vn",
               "Origin": "https://banggia.mbs.com.vn",
               "Referer": "https://banggia.mbs.com.vn/"}
    x = requests.post(url, myobj, verify=False, headers=Headers)

    print(x.content)
    json_x = x.json()['data']
    #
    # print(json_x)
    stock_df = pd.DataFrame()

    for stock in json_x:
        row = {"StockCode": stock['sym'].strip()}
        print(row)
        stock_df = stock_df.append(row, ignore_index=True)

    print(stock_df.head())
    stock_df.to_csv("data/stock_list_" + top_of_floor + ".csv", index=None)

#
# for top_of_floor in ('HNX30',"VN30"):
#     get_top30(top_of_floor)

#011: HNX, 012 HOSE  nếu muốn get cả sàn