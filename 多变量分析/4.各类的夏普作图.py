import pandas as pd
import akshare as ak
import matplotlib.pyplot as plt

target=ak.fund_em_fund_name()
data=pd.read_csv('夏普/sharpe_rate.csv',header=None)
data_index=data[0]
data_sr=data[2]
index_list=list(target['基金代码'])
tag_list=list(target['基金类型'])
tag_type=sorted(list(set(tag_list)))

tag_sr=[]
for tag in tag_type:
    tag_sr.append([])

for i in range(len(data_index)):
    i_str=str(data_index[i])
    if len(i_str)<6:
        index='0'*(6-len(i_str))+i_str
    else:
        index=i_str
    if index in index_list:
        fund_where=index_list.index(index)
        fund_type=tag_list[fund_where]
        fund_type_num=tag_type.index(fund_type)
        tag_sr[fund_type_num].append(data_sr[i])

plt.figure(1)
zero_num=0
for i in range(len(tag_type)):
    plot_sr_data = pd.DataFrame(tag_sr[i])
    if len(tag_sr[i])==0:
        zero_num+=1
    else:
        plt.subplot(3,4,i+1-zero_num)
        plt.hist(tag_sr[i],bins=30,range=[-15,15],density=True,label=tag_type[i]+'\n'+'N='+str(len(tag_sr[i])))
        plt.legend(loc='upper right')
    #plot_sr_data.plot(kind='hist',bins=10,range=[-20,20],normed=True,label='hist')
    #plot_sr_data.plot(kind='kde',color='red',label='kde')
plt.show()
