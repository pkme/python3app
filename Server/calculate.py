# encoding: utf-8

import os   #读取txt文件所需要的包
import linecache

def flt(x):
    return float(x)


file=open('a.txt')    
dataMat=[]  
for line in file.readlines():    
    curLine=line.strip().split(" ")    
    floatLine=list(map(flt,curLine)) #这里使用的是map函数直接把数据转化成为float类型    
    dataMat.append(floatLine[0:3]) 
file.close()

a=dataMat[0][0]
b=dataMat[0][1]
c=a*b
print(a,b,"Result is:",c,)


