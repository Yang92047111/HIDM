from __future__ import print_function
import pandas as pd
from Apriori import *
from FP_growth import *

DataSet = [['M', 'O', 'N', 'K', 'E', 'Y'],
            ['D', 'O', 'N', 'K', 'E', 'Y'],
            ['M', 'A', 'K', 'E'],
            ['M', 'U', 'C', 'K', 'Y'],
            ['C', 'O', 'O', 'K', 'I', 'E']]

L, SupportData = generate_L(DataSet, k = 3, min_support = 0.6)
BigRulesList = generate_big_rules(L, SupportData, min_conf = 0.8)
for Lk in L:
    print ("=" * 50)
    print ("frequent " + str(len(list(Lk)[0])) + "-itemsets\t\tsupport")
    print ("=" * 50)
    for FreqSet in Lk:
        print (FreqSet, SupportData[FreqSet])

minSup = 0.6
initSet = createInitSet(DataSet)
myFPtree, myHeaderTab = createTree(initSet, minSup)
myFPtree.disp()
myFreqList = []
# print(myHeaderTab)
mineTree(myFPtree, myHeaderTab, minSup, set([]), myFreqList)