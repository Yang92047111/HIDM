class treeNode:
    def __init__(self, nameValue, numOccur, parentNode):
        self.name = nameValue       # item name
        self.count = numOccur       # frequency 
        self.nodeLink = None        # pointer to next node with same item name
        self.parent = parentNode    # needs to be updated
        self.children = {}          # next node according to sorting transaction set
    
    def inc(self, numOccur):
        self.count += numOccur
        
    def disp(self, ind=1):
        print('  '*ind, self.name, ' ', self.count)
        for child in self.children.values():
            child.disp(ind+1)

"""Create tree based on given <dataSet>.
    Args:
        dataSet: Input transaction set.
        minSup: Used to filter out infrequent item(s).
        
    Returns:
        retTree: FP-Tree(treeNode) or None if no frequent item
        headerTable: Header table of FP-Tree or None if no frequent item
                     headerTable[item] = (frequency,)
        
    Raises:
        None
"""
def createTree(dataSet, minSup = 1): #create FP-tree from dataset but don't mine
    headerTable = {}
    #go over dataSet twice
    for trans in dataSet:#first pass counts frequency of occurance
        for item in trans:
            headerTable[item] = headerTable.get(item, 0) + dataSet[trans]
    for k in headerTable.keys():  #remove items not meeting minSup
        if headerTable[k] < minSup: 
            del(headerTable[k])
    freqItemSet = set(headerTable.keys())
    #print 'freqItemSet: ',freqItemSet
    if len(freqItemSet) == 0: return None, None  #if no items meet min support -->get out
    for k in headerTable:
        headerTable[k] = [headerTable[k], None] #reformat headerTable to use Node link 
    # print('headerTable: ',headerTable)
    retTree = treeNode('Null Set', 1, None) #create tree
    for tranSet, count in dataSet.items():  #go through dataset 2nd time
        localD = {}
        for item in tranSet:  #put transaction items in order
            if item in freqItemSet:
                localD[item] = headerTable[item][0]
        if len(localD) > 0:
            orderedItems = [v[0] for v in sorted(localD.items(), key=lambda p: p[1], reverse=True)]
            updateTree(orderedItems, retTree, headerTable, count)#populate tree with ordered freq itemset
    return retTree, headerTable #return tree and header table

""" Recursively update the FP-Tree
    Args:
        items: Ordered frequent items
        inTree: FP-Tree node
        headerTable: Header table of FP-Tree
        count: Count of exist same transaction of input items.
        
    Returns:
        None
    
    Raises:
        None
"""
def updateTree(items, inTree, headerTable, count):
    if items[0] in inTree.children:#check if orderedItems[0] in retTree.children
        inTree.children[items[0]].inc(count) #incrament count
    else:   #add items[0] to inTree.children
        inTree.children[items[0]] = treeNode(items[0], count, inTree)
        if headerTable[items[0]][1] == None: #update header table 
            headerTable[items[0]][1] = inTree.children[items[0]]
        else:
            updateHeader(headerTable[items[0]][1], inTree.children[items[0]])
    if len(items) > 1:#call updateTree() with remaining ordered items
        updateTree(items[1::], inTree.children[items[0]], headerTable, count)
        
def updateHeader(nodeToTest, targetNode):   #this version does not use recursion
    while (nodeToTest.nodeLink != None):    #Do not use recursion to traverse a linked list!
        nodeToTest = nodeToTest.nodeLink
    nodeToTest.nodeLink = targetNode
        
"""Ascends from the left node to root and store the path to <prefixPath>.
    Args:
        leafNode: Node of PF-Tree
        prefixPath: list to store the traversal path
        
    Returns:
        None
        
    Raises:
        None
"""        
def ascendTree(leafNode, prefixPath): #ascends from leaf node to root
    if leafNode.parent != None:
        prefixPath.append(leafNode.name)
        ascendTree(leafNode.parent, prefixPath)
        
"""Find prefix path according to given FP-Tree node as <treeNode>
    Args:
        basePat: ?
        treeNode: Target FP-Tree node.
        
    Return:
        condPats: The directory to hold {conditional path->count}
        
    Raises:
        None
"""
def findPrefixPath(basePat, treeNode): #treeNode comes from header table
    condPats = {}
    while treeNode != None:
        prefixPath = []
        ascendTree(treeNode, prefixPath)
        if len(prefixPath) > 1: 
            condPats[frozenset(prefixPath[1:])] = treeNode.count
        treeNode = treeNode.nodeLink
    return condPats

"""Recursively finds frequent itemsets.
    Args:
        inTree: FP-Tree
        headerTable: Header table of FP-Tree
        preFix: Prefix paths
        freqItemList: Frequent item list
        
    Returns:
        None
        
    Raises:
        None
"""
def mineTree(inTree, headerTable, minSup, preFix, freqItemList):
    bigL = [v[0] for v in sorted(headerTable.items(), key = lambda p: str(p[1]))]#(sort header table)
    for basePat in bigL:  #start from bottom of header table
        newFreqSet = preFix.copy()
        newFreqSet.add(basePat)
        #print 'finalFrequent Item: ',newFreqSet    #append to set
        freqItemList.append(newFreqSet)
        condPattBases = findPrefixPath(basePat, headerTable[basePat][1])
        #print 'condPattBases :',basePat, condPattBases
        #2. construct cond FP-tree from cond. pattern base
        myCondTree, myHead = createTree(condPattBases, minSup)
        #print 'head from conditional tree: ', myHead
        if myHead != None: #3. mine cond. FP-tree
            #print 'conditional tree for: ',newFreqSet
            #myCondTree.disp(1)            
            mineTree(myCondTree, myHead, minSup, newFreqSet, freqItemList)

"""Create testing transaction set
    Args:
        None
        
    Returns:
        simpDat: Transaction set
        
    Raises:
        None
"""
def loadSimpDat():
    simpDat = [['r', 'z', 'h', 'j', 'p'],
               ['z', 'y', 'x', 'w', 'v', 'u', 't', 's'],
               ['z'],
               ['r', 'x', 'n', 'o', 's'],
               ['y', 'r', 'x', 'z', 'q', 't', 'p'],
               ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']]
    return simpDat

"""Build up directory to contains (transaction->frequency)
    Args:
        dataSet: Transaction set created by API:loadSimpDat()
        
    Return:
        retDict:
        
    Raise:
        None
"""
def createInitSet(dataSet):
    retDict = {}
    for trans in dataSet:
        retDict[frozenset(trans)] = 1
    return retDict


import twitter
from time import sleep
import re

def textParse(bigString):
    urlsRemoved = re.sub('(http:[/][/]|www.)([a-z]|[A-Z]|[0-9]|[/.]|[~])*', '', bigString)    
    listOfTokens = re.split(r'\W*', urlsRemoved)
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]

def getLotsOfTweets(searchStr):
    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''
    ACCESS_TOKEN_KEY = ''
    ACCESS_TOKEN_SECRET = ''
    api = twitter.Api(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET,
                      access_token_key=ACCESS_TOKEN_KEY, 
                      access_token_secret=ACCESS_TOKEN_SECRET)
    #you can get 1500 results 15 pages * 100 per page
    resultsPages = []
    for i in range(1,15):
        print("fetching page %d" % i)
        searchResults = api.GetSearch(searchStr, per_page=100, page=i)
        resultsPages.append(searchResults)
        sleep(6)
    return resultsPages

def mineTweets(tweetArr, minSup=5):
    parsedList = []
    for i in range(14):
        for j in range(100):
            parsedList.append(textParse(tweetArr[i][j].text))
    initSet = createInitSet(parsedList)
    myFPtree, myHeaderTab = createTree(initSet, minSup)
    myFreqList = []
    mineTree(myFPtree, myHeaderTab, minSup, set([]), myFreqList)
    return myFreqList