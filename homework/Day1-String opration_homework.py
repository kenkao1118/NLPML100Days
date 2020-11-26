# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 11:03:53 2020

@author: Ken_Kao
"""
import pandas as pd

dataset = pd.read_csv("Restaurant_Reviews.tsv",sep='\t')

all_review = dataset['Review'].values

#計算有多少個鋸子是以.結尾

n=0
for line in all_review:
    if(line.endswith('.')):
        n+=1

print('There are {} sentences end with .'.format(n))

#將所有.換成,

n=0
for line in all_review:
    line=line.replace('.',',')
    all_review[n]=line
    n+=1
        
#print(all_review)

#將所有sentence中的第一個the置換為The

n=0
for line in all_review:
    if('the' in line):
        line=line.replace('the','The',1)
        all_review[n]=line
        
    n+=1
#print(all_review)

#將偶數句子全部轉換為大寫,基數句子全部轉換為小寫

n=0
for line in all_review:
    if(n%2==0):
        line=line.upper()
        all_review[n]=line
    else:
        line=line.lower()
        all_review[n]=line      
    n+=1
#print(all_review)

#將所有句子合併在一起,並以'/'為間隔

print('/'.join(all_review))
    








