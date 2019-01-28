#!/usr/bin/env python
# coding: utf-8

# In[5]:


file="retail_dataset.csv"
items=[]
MaxItemId=0
MinItemId=float('inf')
MinSup=10000
MinConf=.7
data=[]


# In[6]:


for line in open(file,'r'):
    transaction=[int(i) for i in line.strip().split(',')]
    MaxItemId=max(MaxItemId,transaction[-1])
    MinItemId=min(MinItemId,transaction[0])
    data.append(set(transaction))


# In[7]:


def GenPowerSet(S):
    
    PowerSet = [set()]

    for Elem in S:
        NewSets = [] 
        for PowerSetItem in PowerSet:
            NewSet = set().union(PowerSetItem) 
            NewSet.add(Elem)
            NewSets.append(NewSet)
        PowerSet.extend(NewSets)

    return PowerSet


# In[8]:


C=[[],[set([i]) for i in range(MinItemId,MaxItemId+1)]]
L=[[]]
Support=[[],[]]
#print(C)

i=1

while 1:
    print('\r'+str(i),end='')
    CurrCandidateSet=C[i]
    LenCurrCandidate=len(CurrCandidateSet)
    SupCount=[0 for j in range(LenCurrCandidate)]
    for transaction in data:
        for j in range(LenCurrCandidate):
            print(str(i)+str(j))
            if len(transaction.intersection(CurrCandidateSet[j]))==len(CurrCandidateSet[j]):
                SupCount[j]+=1
    CurrL=[]
    nextC=[]
    print("done1")
    for j in range(LenCurrCandidate):
        if SupCount[j] >= MinSup:
            CurrL.append(CurrCandidateSet[j])
            Support[i].append(SupCount[j])
    if len(CurrL)==0:
        break
    L.append(CurrL)
   # print("L1:",len(L[1]))
    print("done2")
    for j in range(len(L[i])):
        for k in range(j+1,len(L[i])):
            if len(L[i][j].union(L[i][k]))==i+1 and (L[i][j].union(L[i][k])) not in nextC:
                nextC.append(L[i][j].union(L[i][k]))
                
    C.append(nextC)
    Support.append([])
    i+=1
    
print(L)
#print(Support)
    
    


# In[5]:


FreqItemSet=L[-1]
print(FreqItemSet)
PossRules=[]
StrongRulesL=[]
StrongRulesR=[]


# In[6]:


for i in range(len(FreqItemSet)):
    PossRules=GenPowerSet(FreqItemSet[i])
    LHS=[]
    RHS=[]
    LHS+=PossRules[1:-1]
    for j in range(len(LHS)):
        RHS.append(PossRules[-1]-LHS[j])
    ind=L[len(FreqItemSet[i])].index(FreqItemSet[i])
    ConstNum=Support[len(FreqItemSet[i])][ind]
    for j in range(len(LHS)):
        den=Support[len(LHS[j])][L[len(LHS[j])].index(LHS[j])]
        if (ConstNum/den) >= MinConf:

            StrongRulesL.append(LHS[j])
            StrongRulesR.append(RHS[j])
for i in range(len(StrongRulesL)):
    print(StrongRulesL[i],"=>",StrongRulesR[i])
    
    



# In[ ]:





# In[ ]:




