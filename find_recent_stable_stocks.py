# -*- coding: utf-8 -*-
# author: rw
# E-mail: weiyanjie10@gmail.com
# Todo: find recent stable stocks
import pickle
import datetime
import tushare


count = 0


def get_days():
    today = datetime.date.today()
    days = [today - datetime.timedelta(days=i+1) for i in range(20)]
    def isweekday(day):
        if day.isoweekday() == 7:
            return False
        if day.isoweekday() == 6:
            return False
        return True
    days = filter(isweekday, days)
    return [str(day) for day in days]


def get_all_codes():
    with open("all_codes", "rb") as f:
        codes = pickle.load(f)
    return codes


def get_code_stablity(code):
    global count
    print count
    count += 1
    days = get_days()
    def virance_a_day(day):
        try:
            datas = tushare.get_tick_data(code, date=day, retry_count = 5)
            prices = [value[1] for value in datas.values]
            ave_price = sum(prices) / len(prices)
            virance = sum([(price - ave_price) ** 2 for price in prices])
            return virance
        except:
            return None

    virances = map(virance_a_day, days)
    virances = filter(lambda x:x, virances)
    if virances:
        ave_virances = sum(virances) / len(virances)
    else:
        return None
    return (code, ave_virances)
    

if __name__ == "__main__":
    codes = get_all_codes()
    codes_virances = map(get_code_stablity, codes)
    codes_virances = filter(lambda x:x, codes_virances)
    codes_virances = sorted(codes_virances, key = lambda c_v: c_v[1])
    with open("stable_stocks_today", "wb") as f:
        pickle.dump(codes_virances, f)
