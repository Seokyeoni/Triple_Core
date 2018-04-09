# -*- coding: utf-8 -*-

import pandas as pd
import os
import datetime
#DB에 저장된 정보를 CSV로 하나 유지(모든 파일의 통합) 미리 생성
#csv는 미리 존재해야함

path_csv = "C:/0.bigdata/4.web/Triple_Core/0.DataRepo/0.LocalStorage/csv_data/"
path_info = "C:/0.bigdata/4.web/Triple_Core/0.DataRepo/0.LocalStorage/"
csv_list = os.listdir(path_csv)
info_list = os.listdir(path_info)

def check_symbol_info():
    check_exist_info = [i for i in info_list if i.endswith('.csv')]
    if 'symbol_info.csv' not in check_exist_info:
        symbol_info = pd.DataFrame()
        for file in csv_list:
            symbol_new = pd.read_csv("C:/0.bigdata/4.web/Triple_Core/0.DataRepo/0.LocalStorage/csv_data/"+ file)
            symbol_new.columns = ['Name', 'Symbol', 'Exchange', 'Sector', 'Industry']
            symbol_info=symbol_info.append(symbol_new)
        symbol_info.to_csv("C:/0.bigdata/4.web/Triple_Core/0.DataRepo/0.LocalStorage/symbol_info1.csv", index=False, sep=",", encoding='‘utf-8’')
        
def listing_validation():
    symbol_info = pd.read_csv("C:/0.bigdata/4.web/Triple_Core/0.DataRepo/0.LocalStorage/yesterday_symbol_info_utf8_sample.csv")
    symbol_info["listing"]='x'
    info_vals = symbol_info['Symbol'].values
    for file in csv_list:
        symbol_new = pd.read_csv("C:/0.bigdata/4.web/Triple_Core/0.DataRepo/0.LocalStorage/csv_data/"+file)
        print(symbol_new[:2])
        vals = symbol_new['Symbol'].values
        for symbol in info_vals:
            if symbol in vals:
                symbol_info.loc[symbol_info['Symbol'] == symbol,'listing']='o'
        a = [ symbol for symbol in vals if symbol not in info_vals ]
        if len(a) != 0:
            b = symbol_new[symbol_new['Symbol'] == a]
            b['listing'] = 'New'
            symbol_info = symbol_info.append(b, ignore_index=True)
     
    update_time = datetime.date.today().isoformat()
    symbol_info["updatetime"]=update_time
    symbol_info.name = "a"
    symbol_info.to_csv("C:/0.bigdata/4.web/Triple_Core/0.DataRepo/0.LocalStorage/symbol_info1.csv", index=False, sep=",", encoding='‘utf-8’')

    #불러와서 저장
#check_symbol_info()
#listing_validation()

def listing_validation():
    symbol_info = pd.read_csv("C:/0.bigdata/4.web/Triple_Core/0.DataRepo/0.LocalStorage/yesterday_symbol_info_utf8_sample.csv")
    symbol_info["listing"]='x'
    info_vals = symbol_info['Symbol'].values
    symbol_new = pd.read_csv("C:/0.bigdata/4.web/Triple_Core/0.DataRepo/0.LocalStorage/today_symbol_info_utf8_sample.csv")
#         print(symbol_new[:2])
    vals = symbol_new['Symbol'].values
    for symbol in info_vals:
        if symbol in vals:
            symbol_info.loc[symbol_info['Symbol'] == symbol,'listing']='o'
    a = [ symbol for symbol in vals if symbol not in info_vals ]
    if len(a) != 0:
        for new in a:
            b = symbol_new[symbol_new['Symbol'] == new]
            b['listing'] = 'New'
            symbol_info = symbol_info.append(b, ignore_index=True)

    update_time = datetime.date.today().isoformat()
    symbol_info["updatetime"]=update_time
    symbol_info.name = "a"
    symbol_info.to_csv("C:/0.bigdata/4.web/Triple_Core/0.DataRepo/0.LocalStorage/symbol_info4.csv", index=False, sep=",", encoding='‘utf-8’')
