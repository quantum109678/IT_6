import pandas as pd 
import numpy as np 
 
file="test.csv"
items=[]
MaxItemId=0
MinItemId=float('inf')
MinSup=2
MinConf=50
data=[]
for line in open(file,'r'):
	transaction=[int(i[1:]) for i in line.strip().split(',')]
	MaxItemId=max(MaxItemId,transaction[-1])
	MinItemId=min(MinItemId,transaction[0])
	data.append(set(transaction))

print(data)
C=[[],[set([i]) for i in range(MinItemId,MaxItemId+1)]]
L=[[]]
print(C)

i=1

while 1:
	CurrCandidateSet=C[i]
	LenCurrCandidate=len(CurrCandidateSet)
	SupCount=[0 for j in range(LenCurrCandidate)]
	for transaction in data:
		for j in range(LenCurrCandidate):
			if len(transaction.intersection(CurrCandidateSet[j]))==len(CurrCandidateSet[j]):
				SupCount[j]+=1
	CurrL=[]
	for j in range(LenCurrCandidate):
		if SupCount[j] >= MinSup:
			CurrL.append(CurrCandidateSet[j])
	L.append(CurrL)
	#NextC Generation code and breaking condition
	break




