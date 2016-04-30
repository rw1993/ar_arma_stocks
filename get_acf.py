# -*- coding: utf-8 -*-
# author: rw
# E-mail: weiyanjie10@gmail.com
import pickle
import statsmodels
import datetime
import tushare

def get_maybe_codes():
    with open("stable_stocks_today", "rb") as f:
        codes = pickle.load(f)
    return codes

def get_acf(code):
    print code
    today = datetime.date.today()
    print str(today)
    today_prices = tushare.get_tick_data(code=code, date=str(today),
                                         retry_count=50)
    print today_prices
    today_prices = [(value[0], value[1]) for value in today_prices.values]
    train_prices = [price for time, price in today_prices if time > "13:00:00"]
    print train_prices

if __name__ == "__main__":
    codes = get_maybe_codes()
    get_acf(codes[1000][0])
   
