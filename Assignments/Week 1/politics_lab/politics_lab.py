import sys

voting_data = list(open("voting_record_dump109.txt"))

## Task 1

def create_voting_dict():
    """
    Input: None (use voting_data above)
    Output: A dictionary that maps the last name of a senator
            to a list of numbers representing the senator's voting
            record.
    Example: 
        >>> create_voting_dict()['Clinton']
        [-1, 1, 1, 1, 0, 0, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1]

    This procedure should return a dictionary that maps the last name
    of a senator to a list of numbers representing that senator's
    voting record, using the list of strings from the dump file (strlist). You
    will need to use the built-in procedure int() to convert a string
    representation of an integer (e.g. '1') to the actual integer
    (e.g. 1).

    You can use the split() procedure to split each line of the
    strlist into a list; the first element of the list will be the senator's
    name, the second will be his/her party affiliation (R or D), the
    third will be his/her home state, and the remaining elements of
    the list will be that senator's voting record on a collection of bills.
    A "1" represents a 'yea' vote, a "-1" a 'nay', and a "0" an abstention.

    The lists for each senator should preserve the order listed in voting data. 
    """
    voting_dict = dict()
    for line in voting_data:
        tokens = line.rstrip().split()
        voting_dict[ tokens[0] ] = [ int(x) for x in tokens[3:] ]
    
    return voting_dict
    

## Task 2

def policy_compare(sen_a, sen_b, voting_dict):
    """
    Input: last names of sen_a and sen_b, and a voting dictionary mapping senator
           names to lists representing their voting records.
    Output: the dot-product (as a number) representing the degree of similarity
            between two senators' voting policies
    Example:
        >>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
        >>> policy_compare('Fox-Epstein','Ravella', voting_dict)
        -2
    """
    votes_a = voting_dict.get(sen_a, [])
    votes_b = voting_dict.get(sen_b, [])
    assert len(votes_a)==len(votes_b)
    
    return sum([ votes_a[i]*votes_b[i] for i in range(len(votes_a)) ])


## Task 3

def most_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is most
            like the input senator (excluding, of course, the input senator
            him/herself). Resolve ties arbitrarily.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> most_similar('Klein', vd)
        'Fox-Epstein'

    Note that you can (and are encouraged to) re-use you policy_compare procedure.
    """
    max_similarity = -sys.maxsize
    max_similarity_sen = 'None'
    
    for senator in voting_dict:
        if senator==sen: continue
        
        similarity = policy_compare(sen, senator, voting_dict)
        if  similarity > max_similarity:
            max_similarity_sen = senator
            max_similarity = similarity
    
    return max_similarity_sen
    

## Task 4

def least_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is least like the input
            senator.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> least_similar('Klein', vd)
        'Ravella'
    """
    min_similarity = sys.maxsize
    min_similarity_sen = 'None'
    
    for senator in voting_dict:
        if senator==sen: continue
        
        similarity = policy_compare(sen, senator, voting_dict)
        if  similarity < min_similarity:
            min_similarity_sen = senator
            min_similarity = similarity
    
    return min_similarity_sen
    
    

## Task 5
voting_dict = create_voting_dict()

most_like_chafee = most_similar('Chafee', voting_dict)
least_like_santorum = least_similar('Santorum', voting_dict)

print('Most like Chafee: %s' % most_like_chafee)
print('Least like Santorum: %s' % least_like_santorum)
print('Boxer vs. Feinstein: %0.2f' % policy_compare('Boxer', 'Feinstein', voting_dict))

# Task 6

def find_average_similarity(sen, sen_set, voting_dict):
    """
    Input: the name of a senator, a set of senator names, and a voting dictionary.
    Output: the average dot-product between sen and those in sen_set.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> find_average_similarity('Klein', {'Fox-Epstein','Ravella'}, vd)
        -0.5
    """
    similarity_sum = 0
    for senator in sen_set:
        if senator==sen: continue
        
        similarity_sum += policy_compare(sen, senator, voting_dict)
        
    return float(similarity_sum)/len(sen_set)
    
# create voting_dict with only Democrats
democrat_senators = set()
for line in voting_data:
    senator, party = line.split()[0:2]
    if party=='D':
        democrat_senators.add(senator)

# find Democratic senator with largest average similarity to other Democrats
max_average_similarity = -sys.maxsize
most_average_Democrat = 'None'

for senator in democrat_senators:
    average_similarity = find_average_similarity(senator, democrat_senators, voting_dict)
    if average_similarity > max_average_similarity:
        max_average_similarity = average_similarity
        most_average_Democrat = senator

print('Most average Democratic senator: %s (score %0.2f)' % (most_average_Democrat, max_average_similarity))

# Task 7

def find_average_record(sen_set, voting_dict):
    """
    Input: a set of last names, a voting dictionary
    Output: a vector containing the average components of the voting records
            of the senators in the input set
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> find_average_record({'Fox-Epstein','Ravella'}, voting_dict)
        [-0.5, -0.5, 0.0]
    """
    record_sum = []
    for senator in sen_set:
        if len(record_sum)==0: record_sum = voting_dict[ senator ]
        else: record_sum = [ x+y for x,y in zip(record_sum, voting_dict[ senator ]) ]
        
    return [ float(x)/len(sen_set) for x in record_sum ]

average_Democrat_record = find_average_record(democrat_senators, voting_dict)
test_voting_dict = voting_dict.copy()
test_voting_dict[ 'average_democrat' ] = average_Democrat_record

print('Most average Democratic senator by comparison to average: %s' % most_similar('average_democrat', test_voting_dict))
del(test_voting_dict)

# Task 8

def bitter_rivals(voting_dict):
    """
    Input: a dictionary mapping senator names to lists representing
           their voting records
    Output: a tuple containing the two senators who most strongly
            disagree with one another.
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> bitter_rivals(voting_dict)
        ('Fox-Epstein', 'Ravella')
    """
    senator_list = list(voting_dict.keys())
    min_similarity = sys.maxsize
    senator_a = senator_b = "None"
    
    for i in range(len(senator_list)-1):
        for j in range(i+1, len(senator_list)):
            similarity = policy_compare(senator_list[i], senator_list[j], voting_dict)
            
            if similarity < min_similarity:
                min_similarity = similarity
                senator_a = senator_list[i]
                senator_b = senator_list[j]
    
    return (senator_a, senator_b)

rival_senators = bitter_rivals(voting_dict)
print('Senators with most opposing records: %s %s' % (rival_senators[0], rival_senators[1]))
