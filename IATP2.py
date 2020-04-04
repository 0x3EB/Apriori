# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 16:26:23 2020

@author: sebas
"""

def createCk(data,e,Lk=None,k=2):
    k+=1
    Ck = []
    test = []
    aa = []
    ScanC = {}
    if Lk is not None:
        ScanC.update(Lk)
        if len(Lk) > 1:
            t = list(Lk.keys())
            for i in range(0,len(Lk)-1):
                for j in range(i,len(Lk)-1):
                    if type(t[i]) == int and type(t[j+1] == int):
                        Ck.append([t[i],t[j+1]])
                    elif type(t[i]) == tuple and type(t[j+1] == tuple):
                        in_first = set(list(t[i]))
                        in_second = set(list(t[j+1]))
                        in_second_but_not_in_first = in_second - in_first
                        result = list(t[i]) + list(in_second_but_not_in_first)
                        print(result)
                        if not (all(elem in result for elem in aa)) and len(result)==k: aa.append(result)
            #Ck.sort()
            print(aa)
            # isinstance !!!!!
            for i in data:
                for j in Ck:
                    if (type(i) == list and type(j) == list):
                        if(all(elem in i for elem in j)):
                            test.append(tuple(j))
            bb = []
            for i in data:
                for j in aa:
                    if (type(i) == list and type(j) == list):
                        if(all(elem in i for elem in j)):
                            print(bb)
                            if j not in bb: bb.append(tuple(j))
            if len(test)>0:
                ScanC.update({x : test.count(x) for x in test if test.count(x)>=e})
            if len(bb)>0:
                ScanC.update({x : bb.count(x) for x in bb if bb.count(x)>=e})
            #createCk(data,e,ScanC,k)
    else:     
        for transaction in data:
            for item in transaction:
                if not [transaction,item] in Ck: Ck.append(item)
        ScanC = {x : Ck.count(x) for x in Ck if Ck.count(x)>=e}
        createCk(data,e,ScanC,k)
    return ScanC

def apriori(T,e):
    res = {}
    res.update(createCk(T,e,createCk(T,e,createCk(T,e))))
    print(res)

if __name__ == '__main__':
    dataset = [[1, 2, 5], [1, 3, 5], [1, 2], [1, 2, 3, 4, 5], [1, 2, 4, 5], [2, 3, 5], [1, 5]]
    apriori(dataset,3)