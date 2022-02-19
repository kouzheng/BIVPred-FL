import os
import re
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib

def pr(ft_type):
    if ft_type=='1':
        f=open('mrmr_hot.csv','r')
        myft=[]
        for each in f:
            myft.append(each.rstrip())
        f.close

        mypred={}
        myid=[]
        for i in range(67):
            temp= pd.read_csv('./feature/'+myft[i]+'.csv',header=None)
            mydata=temp.values
            rf=joblib.load('./model/'+myft[i])
            hot=rf.predict(mydata[:,1:])
            for j in range(len(hot)):
                if i==0:
                    mypred[mydata[j,0]]=mydata[j,0]+','+str(hot[j])
                    myid.append(mydata[j,0])
                else:
                    mypred[mydata[j,0]]+=','+str(hot[j])

        fw=open('pred_hot.csv','w+')
        for each in myid:
            fw.write(mypred[each]+'\n')
        fw.close

    if ft_type=='2':
        f=open('mrmr_val.csv','r')
        myft=[]
        for each in f:
            myft.append(each.rstrip())
        f.close

        mypred={}
        myid=[]
        for i in range(67):
            temp= pd.read_csv('./feature/'+myft[i]+'.csv',header=None)
            mydata=temp.values
            rf=joblib.load('./model/'+myft[i])
            hot=rf.predict_proba(mydata[:,1:])
            for j in range(len(hot)):
                if i==0:
                    mypred[mydata[j,0]]=mydata[j,0]+','+str(hot[j,1])
                    myid.append(mydata[j,0])
                else:
                    mypred[mydata[j,0]]+=','+str(hot[j,1])

        fw=open('pred_val.csv','w+')
        for each in myid:
            fw.write(mypred[each]+'\n')
        fw.close




            
