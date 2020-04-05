# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 16:26:23 2020
@author: sebas
"""

def createLk(data,e,Lk=None,k=1):
    Ck = []
    tupleNPreviousplets = []
    listNplets = []
    tupleNplets = []
    ScanC = {}
    if Lk is None:
        for transaction in data:
            for item in transaction:
                if not [transaction,item] in Ck: Ck.append(item)
        ScanC = {x : Ck.count(x) for x in Ck if Ck.count(x)>=e}
    else:
        ScanC.update(Lk)
        keys = list(Lk.keys())
        for i in range(0,len(Lk)-1):
            for j in range(i,len(Lk)-1):
                if isinstance(keys[i],int) and isinstance(keys[j+1],int):
                    Ck.append([keys[i],keys[j+1]])
                elif isinstance(keys[i],tuple) and isinstance(keys[j+1],tuple):
                    in_first = set(list(keys[i]))
                    in_second = set(list(keys[j+1]))
                    in_second_but_not_in_first = in_second - in_first
                    result = list(keys[i]) + list(in_second_but_not_in_first)
                    if (all(elem in result for elem in listNplets)) and len(result)==k: listNplets.append(result)
        for i in data:
            for j in Ck:
                if isinstance(i,list) and isinstance(j,list):
                    if(all(elem in i for elem in j)):
                        tupleNPreviousplets.append(tuple(j))
        for i in data:
            for j in listNplets:
                if isinstance(i,list) and isinstance(j,list):
                    if(all(elem in i for elem in j)):
                        if j not in tupleNplets: tupleNplets.append(tuple(j))
        if len(tupleNPreviousplets)>0: ScanC.update({x : tupleNPreviousplets.count(x) for x in tupleNPreviousplets if tupleNPreviousplets.count(x)>=e})
        if len(tupleNplets)>0: ScanC.update({x : tupleNplets.count(x) for x in tupleNplets if tupleNplets.count(x)>=e})
        if len(Lk) == len(ScanC):
            return ScanC
    return createLk(data,e,ScanC,k+1)

def apriori(T,e):
    return createLk(T,e)

if __name__ == '__main__':
    dataset = [[1, 2, 5], [1, 3, 5], [1, 2], [1, 2, 3, 4, 5], [1, 2, 4, 5], [2, 3, 5], [1, 5]]
    dataset2 = [[1, 3, 4], [2,3, 5], [1, 2, 3, 5], [2, 5]]
    L = apriori(dataset2,2)
    print(L)