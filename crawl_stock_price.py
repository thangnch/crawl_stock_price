import pandas as pd
import requests
import csv

def get_main_index(StockCode, hnx30_list, vn30_list):
    if [StockCode] in hnx30_list:
        return "HNX30"
    elif [StockCode] in vn30_list:
        return "VN30"
    else:
        return "NULL"

def get_price_at_date(date_to_get):
    # Prepare
    file = open("data/stock_list_hnx30.csv", "r")
    hnx30_list = list(csv.reader(file, delimiter="-"))[1:]
    print(hnx30_list)
    file.close()

    file = open("data/stock_list_vn30.csv", "r")
    vn30_list = list(csv.reader(file, delimiter="-"))[1:]
    print(vn30_list)
    file.close()


    url = "https://finfo-api.vndirect.com.vn/v4/stock_prices?sort=date&q=date:{}~floor:HNX,HOSE&size=9990&page=1".format(date_to_get)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    print(url)
    x = requests.get(url,verify=True, headers=headers)

    print(x)
    stock_price_df = pd.DataFrame()
    json_x = x.json()['data']
    for stock in json_x:
        print(stock)
        stock_price_df = stock_price_df.append({
            "Date": date_to_get,
            "StockCode": stock['code'],
            "ATC": stock['close'],
            "Floor": stock['floor'],
            "MainIndex":get_main_index(stock['code'], hnx30_list, vn30_list),
            "PSGD": "CHIU"
        }, ignore_index=True)

    stock_price_df.to_csv("data/stock_price.csv", index=None)
    stock_price_df.to_csv("static/stock_price_{}.csv".format(date_to_get), index=None)

# get_price_at_date('2023-04-28')