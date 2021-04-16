# -*- coding: utf-8 -*-

import pandas as pd
import math


file_path = 'C:/Users/cecks/Downloads/'
file_name = '^N225.csv'


# read csv and insert colmn
stock_csv = pd.read_csv(file_path + file_name)
stock_csv['LogClose'] = ''


# len long
maxlength = len(stock_csv)


# log = log(today close/beforeday close)
for length_no in range(1, maxlength):
    stock_csv['LogClose'][length_no] = math.log(float(stock_csv['Close'][length_no]), float(stock_csv['Close'][length_no - 1]))


stock_csv.to_csv(file_path + 'addlog' + file_name)