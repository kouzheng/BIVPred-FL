import re
from Bio import SeqIO
import numpy as np

def ft(fname):
    # GGAP
    kv={}
    f=open("AAfactor.csv","r")
    for each in f:
        temp=re.split(",",each.rstrip())
        kv[temp[0]]=each.rstrip()
    f.close

    myvalue={}
    ky1=kv.keys()
    ky2=kv.keys()

    for nnn in range(18):
        for i in range(21):
            for j in range(21):
                myvalue[ky1[i]+ky2[j]]=0
                
        fw=open('./feature/'+'GGAP_'+str(nnn)+'.csv','w+')
        for each in SeqIO.parse(fname, "fasta"):
            fw.write(each.id)
            temp=str(each.seq)

            for i in range(len(temp)):
                myvalue[temp[i]+temp[(i+nnn+1)%len(temp)]]+=1        

            for xxx in myvalue.keys():
                yyy=float(myvalue[xxx])/len(temp)
                myvalue[xxx]=yyy

            for i in range(21):
                for j in range(21):
                    fw.write(','+str(myvalue[ky1[i]+ky2[j]]))
            fw.write('\n')
        fw.close
        
    # AAC PC-PseAAC
    kv={}
    f=open("AAfactor.csv","r")
    for each in f:
        temp=re.split(",",each.rstrip())
        kv[temp[0]]=each.rstrip()
    f.close

    myvalue={}
    ky1=kv.keys()
    ky2=kv.keys()

    for i in range(21):
        for j in range(21):
            temp1=kv[ky1[i]]
            temp2=kv[ky2[j]]

            xxx=re.split(",",temp1)
            yyy=re.split(",",temp2)

            zzz=0
            for k in range(5):
                zzz+=(float(xxx[k+1])-float(yyy[k+1]))*(float(xxx[k+1])-float(yyy[k+1]))

            myvalue[xxx[0]+yyy[0]]=zzz/5


    fw1=open('./feature/'+'AAC.csv','w+')
    for nnn in range(18):
        fw=open('./feature/'+'PC-PseAAC_'+str(nnn)+'.csv','w+')
        
        
        for each in SeqIO.parse(fname, "fasta"):
            temp=str(each.seq)
            xxx={}
        
            for i in range(nnn+1):
                uu=0
                for j in range(len(temp)):
                    uu+=myvalue[temp[j]+temp[(j+i+1)%len(temp)]]
                xxx[i+21]=uu/len(temp)

            arr=[]
            for l in range(21):
                arr.append(float(temp.count(ky1[l]))/len(temp))

            
            arr_mean=np.mean(arr)
            arr_std=np.std(arr,ddof=1)

            for l in range(21):
                xxx[l]=(arr[l]-arr_mean)/arr_std

            myt=0
            for m in range(21+nnn+1):
                if m<21:
                    myt+=xxx[m]
                else:
                    myt+=0.05*xxx[m]
            
            
            fw.write(each.id)
            for m in range(21+nnn+1):
                if m<21:
                    fw.write(','+str(xxx[m]/myt))
                else:
                    fw.write(','+str(0.05*xxx[m]/myt))
            fw.write('\n')

            if nnn==0:
                fw1.write(each.id)
                for m in range(21):         
                    fw1.write(','+str(xxx[m]))
                fw1.write('\n')
            
        fw.close
    fw1.close 

    # OLP
    kv={}
    f=open("AAfactor.csv","r")
    for each in f:
        temp=re.split(",",each.rstrip())
        kv[temp[0]]=''
    f.close

    f=open("OLP.csv","r")
    for each in f:
        temp=re.split("}",each)
        xxx=re.split("{",temp[0])
        for myaa in kv.keys():
            if myaa in xxx[1]:
                kv[myaa]+=',1'
            else:
                kv[myaa]+=',0'
    f.close

    mypos={}
    f=open('OLP-BIT-position.csv','r')
    for each in f:
        temp=re.split(',',each.rstrip())
        mypos[int(temp[3])-1]=int(temp[1])-1
    f.close

    for i in range(10):     
        fw=open('./feature/'+'OLP_'+str(4*(i+1))+'.csv','w+')
        for seq_record in SeqIO.parse(fname,'fasta'):
            st=list(str(seq_record.seq))
            sta=[]
            for xx in range(len(st)):
                sta.append(st[mypos[xx]])
            myseq=''.join(sta)
            fw.write(seq_record.id)
            for k in range(i+1):
                for j in range(4):
                    fw.write(kv[myseq[k*4+j]])
            fw.write('\n')            
        fw.close


    # BIT21
    kv={}
    f=open("AAfactor.csv","r")
    for each in f:
        temp=re.split(",",each.rstrip())
        kv[temp[0]]=''
    f.close

    for i in range(5):
        f=open('f'+str(i+1)+'_cl.csv',"r")
        for each in f:
            temp=re.split(",",each.rstrip())
            kv[temp[0]]+=','+temp[1]+','+temp[2]+','+temp[3]+','+temp[4]
        f.close

    for i in range(10):     
        fw=open('./feature/'+'BIT21_'+str(4*(i+1))+'.csv','w+')
        for seq_record in SeqIO.parse(fname,'fasta'):
            st=list(str(seq_record.seq))
            sta=[]
            for xx in range(len(st)):
                sta.append(st[mypos[xx]])
            myseq=''.join(sta)
            fw.write(seq_record.id)
            for k in range(i+1):
                for j in range(4):
                    fw.write(kv[myseq[k*4+j]])
            fw.write('\n')             
        fw.close


    # BIT20
    kv={}
    f=open("AAfactor.csv","r")
    for each in f:
        temp=re.split(",",each.rstrip())
        kv[temp[0]]=''
    f.close

    f=open("AAfactor.csv","r")
    num=0
    for each in f:
        temp=re.split(",",each.rstrip())
        for i in range(21):
            if i==num:
                kv[temp[0]]+=',1'
            else:
                kv[temp[0]]+=',0'
        num+=1
    f.close

    for i in range(10):     
        fw=open('./feature/'+'BIT20_'+str(4*(i+1))+'.csv','w+')
        for seq_record in SeqIO.parse(fname,'fasta'):
            st=list(str(seq_record.seq))
            sta=[]
            for xx in range(len(st)):
                sta.append(st[mypos[xx]])
            myseq=''.join(sta)
            fw.write(seq_record.id)
            for k in range(i+1):
                for j in range(4):
                    fw.write(kv[myseq[k*4+j]])
            fw.write('\n')             
        fw.close
                


    
