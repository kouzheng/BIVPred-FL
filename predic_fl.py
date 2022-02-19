import os
import re
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib

def prfl(ft_type,ft_num,pconf):
    if ft_type=='1':
        temp= pd.read_csv('ft_hot.csv',header=None)
        mydata=temp.values
        model=RandomForestClassifier(n_estimators=500,random_state=0,n_jobs=-1)
        rf=model.fit(mydata[:,1:(ft_num+1)],mydata[:,0])

        temp= pd.read_csv('pred_hot.csv',header=None)
        mydata=temp.values
        hot=rf.predict_proba(mydata[:,1:(ft_num+1)])

        fw=open('predicting_results.csv','w+')
        for i in range(len(hot)):
            if hot[i,1]>=pconf:
                fw.write(mydata[i,0]+','+'P'+'\n')
            else:
                fw.write(mydata[i,0]+','+'N'+'\n') 
        fw.close

        print "DONE!"

    if ft_type=='2':
        temp= pd.read_csv('ft_val.csv',header=None)
        mydata=temp.values
        model=RandomForestClassifier(n_estimators=500,random_state=0,n_jobs=-1)
        rf=model.fit(mydata[:,1:(ft_num+1)],mydata[:,0])

        temp= pd.read_csv('pred_val.csv',header=None)
        mydata=temp.values
        hot=rf.predict_proba(mydata[:,1:(ft_num+1)])

        fw=open('predicting_results.csv','w+')
        for i in range(len(hot)):
            if hot[i,1]>=pconf:
                fw.write(mydata[i,0]+','+'P'+'\n')
            else:
                fw.write(mydata[i,0]+','+'N'+'\n')
        fw.close

        print "DONE!"


            
