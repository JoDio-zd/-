data1<-read.csv("../data/mix.csv",header = T)
data2<-read.csv("../data/QDII.csv",header = T)
data3<-read.csv("../data/FOF.csv",header = T)
data4<-read.csv("../data/stock.csv",header = T)
data5<-read.csv("../data/exp.csv",header = T)
data6<-read.csv("../data/bond.csv",header = T)
data7<-read.csv("../data/LOF.csv",header = T)

head(data1)
data1$类型<-"mix"
data2$类型<-"QDII"
data3$类型<-"FOF"
data4$类型<-"ttock"
data5$类型<-"exp"
data6$类型<-"bond"
data7$类型<-"LOF"

nrow(data1)
nrow(data2)
data<-rbind(data1,data2,data3,data4,data5,data6,data7)
data$类型<-as.factor(data$类型)
head(data)
nrow(data)
data$类型[1]

#数据处理
data<-data[!is.na(data$单位净值),]
table(is.na(data$单位净值))
data<-data[!is.na(data$累计净值),]
table(is.na(data$累计净值))
data<-data[!is.na(data$近6月),]
table(is.na(data$近6月))


data[is.na(data$日增长率),8]<-mean(data$日增长率,na.rm = T)
table(is.na(data$日增长率))
data[is.na(data$近1周),9]<-mean(data$近1周,na.rm = T)
table(is.na(data$近1周))
data[is.na(data$近1月),10]<-mean(data$近1月,na.rm = T)
table(is.na(data$近1月))
data[is.na(data$近3月),11]<-mean(data$近3月,na.rm = T)
table(is.na(data$近3月))
data[is.na(data$近1年),13]<-mean(data$近1年,na.rm = T)
table(is.na(data$近1年))
data[is.na(data$近2年),14]<-mean(data$近2年,na.rm = T)
table(is.na(data$近2年))
data[is.na(data$近3年),15]<-mean(data$近3年,na.rm = T)
table(is.na(data$近3年))
data[is.na(data$今年来),16]<-mean(data$今年来,na.rm = T)
table(is.na(data$今年来))

colnames(data)[c(6:17,20)]

wssplot<-function(data,nc=15,seed=1234){
  wss<-(nrow(data)-1)*sum(apply(data,2,var))
  for(i in 2:nc){
    set.seed(seed)
    wss[i]<-sum(kmeans(data,centers = i)$withinss)
  }
  plot(1:nc,wss,type="b",xlab="Number of Clusters",ylab=("Within groups sum of aquares"))
}
levels(data$类型)
df<-scale(data[,c(6:17)])
df<-cbind(df,data$类型)
ncol(df)
class(df[,13])
colnames(df)[13]<-"类型"
for(i in 1:13)print(table(is.na(df[,i])))
wssplot(df)
library(NbClust)
set.seed(1234)
fit.km<-kmeans(df,3,nstart=25)
fit.km$size
fit.km$centers
levels(data$类型)
aggregate(df,by=list(cluster=fit.km$cluster),FUN=mean)
aggregate(df,by=list(cluster=fit.km$cluster),var)
aggregate(as.numeric(data$类型),by=list(cluster=fit.km$cluster),FUN=mean)
levels(data$类型)

