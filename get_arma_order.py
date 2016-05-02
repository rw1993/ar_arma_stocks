# -*- coding: utf-8 -*-
# author: rw
# E-mail: weiyanjie10@gmail.com
import pickle
from statsmodels.tsa import ar_model
import datetime
import tushare

def get_maybe_codes():
    with open("stable_stocks_today", "rb") as f:
        codes = pickle.load(f)
    return codes

def get_last_day():
    today = datetime.date.today()
    if today.isoweekday() == 7:
        return today - datetime.timedelta(days=2)
    elif today.isoweekday() == 6:
        return today - datetime.timedelta(days=1)
    return today

def get_acf(code):
    day = get_last_day()
    print str(day)
    today_prices = tushare.get_tick_data(code=code,
                                         date=str(day-datetime.timedelta(days=3)),
                                         retry_count=50)
    today_prices = [(value[0], value[1]) for value in today_prices.values]
    train_prices = [price for time, price in today_prices if time > "13:00:00"]
    return ar_model.AR.fit(train_prices)

if __name__ == "__main__":
    codes = get_maybe_codes()
    print get_acf(codes[1][0])
   
