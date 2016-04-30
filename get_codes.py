# -*- coding: utf-8 -*-
# author: rw
# E-mail: weiyanjie10@gmail.com
# get_codes.py get codes using tushare
import tushare
import pickle


def get_codes():
    codes = tushare.get_industry_classified()
    codes = [value[0] for value in codes.values]
    with open("all_codes", "wb") as f:
        pickle.dump(codes, f)
    return codes


if __name__ == "__main__":
    print len(get_codes())
