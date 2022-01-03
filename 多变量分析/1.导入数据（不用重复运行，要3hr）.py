import akshare as ak
import csv
import time
t0=time.time()
open_list = ak.fund_em_open_fund_daily()
open_list.to_csv('夏普/fund_list.csv')
open_index=open_list['基金代码']
t1=time.time()
with open('夏普/histdata.csv','w',newline='') as hist_file:
    writer = csv.writer(hist_file)
    for i in range(len(open_index)):
        if i < 100000:
            hist_data = ak.fund_em_open_fund_info(fund=open_index[i],indicator='累计净值走势')
            hist_data_reverse=list(hist_data.iloc[:, 1])
            hist_data_reverse.reverse()
            if len(hist_data_reverse) < 250:
                row = hist_data_reverse + ['nan']*(250-len(hist_data_reverse))
            else:
                row = hist_data_reverse[:250]
            writer.writerow(row)
hist_file.close()
t2=time.time()
print(t1-t0)
print(t2-t1)

