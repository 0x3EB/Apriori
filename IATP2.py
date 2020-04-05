# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 16:26:23 2020
@author: sebastien lejeune A3 alternance IBO
"""
def createLk(data,e,Lk=None,k=1):
    '''
    Recursive function for frequent item set mining and association rule learning
    Parameters
    ----------
    data : Array of Array
        Data contains the initial dataset.
    e : int
        The number min of occurence (min support).
    Lk : Dictonnary, optional
        Lk is the previous itemset. The default is None.
    k : int, optional
        k is the level of item set (Lk)

    Returns
    -------
    Dictionary
        A dictionary with all the Lk (itemset) depending their occurences.

    '''
    Ck = [] #creating the Ck of the k level
    tupleNPreviousplets = [] #list that contains all the tuples of previous itemset
    listNplets = [] #list that contains itemset in list
    tupleNplets = [] #list that contains itemset in tuples
    noDup = [] # tab that contains no duplicates itemset
    ScanC = {} #dictionnary that will contains all the itemset
    if Lk is None: #check if Lk has been pass in parameters or not
        for transaction in data:
            for item in transaction:
                if not [transaction,item] in Ck: Ck.append(item)
        ScanC = {x : Ck.count(x) for x in Ck if Ck.count(x)>=e} #generating the first Lk (L1)
    else:
        ScanC.update(Lk) #update ScanC with the data of Lk
        keys = list(Lk.keys()) #retrieve all keys of Lk that permit to create couples,triplets,...
        for i in range(0,len(Lk)-1):
            for j in range(i,len(Lk)-1):
                if isinstance(keys[i],tuple) and isinstance(keys[j+1],tuple):#check if the key is a tuple
                    in_first = set(list(keys[i]))
                    in_second = set(list(keys[j+1]))
                    in_second_but_not_in_first = in_second - in_first
                    result = list(keys[i]) + list(in_second_but_not_in_first) #remove duplicates
                    if len(result)==k:listNplets.append(result) #if the length of result is the same as the level of Lk juste add in the listNplets list
                else:#if it is not a tuple juste create a couple
                    Ck.append([keys[i],keys[j+1]])
        for i in listNplets:
            i.sort()
            if i not in noDup: noDup.append(i) #remove duplicates
        for i in noDup:
            for d in data:
                if (all(elem in d for elem in i)) and len(i)==k:
                    tupleNplets.append(tuple(i)) #set all lists in tuples
        for i in data:
            for j in Ck:
                if(all(elem in i for elem in j)):
                   tupleNPreviousplets.append(tuple(j)) #set all lists in tuples
        if len(tupleNPreviousplets)>0: ScanC.update({x : tupleNPreviousplets.count(x) for x in tupleNPreviousplets if tupleNPreviousplets.count(x)>=e}) #add to the dictonnary ScanC the key (the tuple) and the value (the number of count of the key in the original data)
        if len(tupleNplets)>0: ScanC.update({x : tupleNplets.count(x) for x in tupleNplets if tupleNplets.count(x)>=e}) #add to the dictonnary ScanC the key (the tuple) and the value (the number of count of the key in the original data)
        if len(Lk) == len(ScanC):
            return ScanC #return the final dict if ScanC and Lk has the same length
    return createLk(data,e,ScanC,k+1) #add recursive to go in the next level of K if there are itemset

def apriori(T,e):
    '''
    The frequent item sets determined by Apriori can be used to determine association rules which highlight general trends
    '''
    return createLk(T,e) #return a dict

if __name__ == '__main__':
    # TESTING DATA
    dataset = [[1, 2, 5], [1, 3, 5], [1, 2], [1, 2, 3, 4, 5], [1, 2, 4, 5], [2, 3, 5], [1, 5]]
    dataset2 = [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5], [1, 3, 5]]
    dataset3 = [[1, 2, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5], [1, 3, 5], [1, 5], [2, 3, 4], [1, 3, 4, 5]]
    datasetString = [['A','C','D'],['B','C','E'],['A','B','C','E'],['B','E']]
    L = apriori(datasetString,2)
    print(L)