from random import randint
from dictutil import *

## Task 1
def movie_review(name):
    """
    Input: the name of a movie
    Output: a string (one of the review options), selected at random using randint
    """
    review_options = ["See it!", "A gem!", "Ideological claptrap!"]
    return review_options[randint(0, len(review_options)-1)]

## Tasks 2 and 3 are in dictutil.py

## Task 4    
def makeInverseIndex(strlist):
    """
    Input: a list of documents as strings
    Output: a dictionary that maps each word in any document to the set consisting of the
            document ids (ie, the index in the strlist) for all documents containing the word.

    Note that to test your function, you are welcome to use the files stories_small.txt
      or stories_big.txt included in the download.
    """
    invIndex = dict()
    
    for i, line in enumerate(strlist):
        #print("line %d length %d" % (i, len(strlist[i])))
        
        for word in line.rstrip().split():
            if word not in invIndex:
                wordSet = set()
                invIndex[ word ] = wordSet
            else:
                wordSet = invIndex[ word ]
            
            wordSet.add(i)
        
            
    return invIndex 
    

## Task 5
def orSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of document ids that contain _any_ of the specified words
    """
    outputSet = set()
    
    for word in query:
        if word in inverseIndex:
            outputSet = outputSet | inverseIndex[ word ]
    
    return outputSet

## Task 6
def andSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of all document ids that contain _all_ of the specified words
    """
    outputSet = set()
    for valueSet in inverseIndex.values():
        outputSet = outputSet | valueSet
    
    for word in query:
        if word in inverseIndex:
            outputSet = outputSet & inverseIndex[ word ]
    
    return outputSet
