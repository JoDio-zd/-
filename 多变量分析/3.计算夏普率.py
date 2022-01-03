import pandas as pd
import numpy as np
import csv
import math
fund=pd.read_csv('夏普/fund_list.csv',encoding='utf-8')
data=pd.read_csv('夏普/history_rate.csv',encoding='utf-8',header=None)
interest_rate=pow(1.03,1/250)-1

with open('夏普/sharpe_rate.csv','w',newline='') as sharpe_file:
    writer=csv.writer(sharpe_file)
    for i in range(len(data)):
        if i <10000:
            row=[]
            rating_data=list(data.iloc[i])
            data_std=np.nanstd(rating_data)
            data_mean=np.nanmean(rating_data)
            sharpe_rate=(data_mean-interest_rate)/data_std*math.sqrt(250)
            nan_num=np.isnan(rating_data).sum()
            row.append(fund['基金代码'][i])
            row.append(fund['基金简称'][i])
            row.append(sharpe_rate)
            row.append(249-nan_num)
            writer.writerow(row)
sharpe_file.close()


