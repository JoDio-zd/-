import pandas as pd
import csv
import math
import time
t1=time.time()
hist_file=pd.read_csv('夏普/histdata.csv',encoding='utf-8',header=None)
with open('夏普/history_rate.csv','w',newline='') as rate_file:
    writer=csv.writer(rate_file)
    writer.writerow(['基金代码','基金简称','夏普率','有效建立时间'])
    for i in range(len(hist_file)):
        row = []
        if i < 10000:
            for day in range(249):
                if not math.isnan(hist_file.loc[i][day+1]):
                    row.append((hist_file.loc[i][day]-hist_file.loc[i][day+1])/hist_file.loc[i][day+1])
                else:
                    row.append('nan')
            writer.writerow(row)
rate_file.close()
t2=time.time()
print(t2-t1)