# Caroline Briggs
# Python implementation of stable matching problem
# Homework 1 Starter Code
# CYB 2013

def gs(men, women, pref):
    """
    Gale-shapley algorithm, modified to exclude unacceptable matches
    Inputs: men (list of men's names)
            women (list of women's names)
            pref (dictionary of preferences mapping names to list of preferred names in sorted order)
            blocked (list of (man,woman) tuples that are unacceptable matches)
    Output: dictionary of stable matches
    """
    # preprocessing
    ## build the rank dictionary
    rank={}
    for w in women:
        rank[w] = {}
        i = 1
        for m in pref[w]:
            rank[w][m]=i
            i+=1
    ## create a "pointer" to the next woman to propose
    prefptr = {}
    for m in men:
        prefptr[m] = 0

    freemen = set(men)    #initially all men and women are free
    numpartners = len(men) 
    S = {}           #build dictionary to store engagements 

    #run the algorithm
    while freemen:
        m = freemen.pop()
        #get the highest ranked woman that has not yet been proposed to
        w = pref[m][prefptr[m]]
        prefptr[m]+=1
        if w not in S: S[w] = m
        else:
            mprime = S[w]
            if rank[w][m] < rank[w][mprime]:
                S[w] = m
                freemen.add(mprime)
            else:
                freemen.add(m)
    return S

def gs_block(men, women, pref, blocked):
    """
    Gale-Shapley algorithm, modified to exclude unacceptable matches.
    
    Inputs:
        men (list): List of men's names.
        women (list): List of women's names.
        pref (dict): Dictionary mapping each person to their preference list.
        blocked (list): List of (man, woman) tuples that are unacceptable matches.
    
    Output:
        dict: Stable matches as a dictionary mapping men to women.
    """
    # build the rank dictionary
    rank = {w: {m: i for i, m in enumerate(pref[w])} for w in women}
  
    # create pointer
    prefptr = {m: 0 for m in men}

    # track current freemen and which matches are blocked
    freemen = set(men)
    S = {}  # woman → man
    blocked_set = set(blocked)

    # run the algorithm
    while freemen:
        m = freemen.pop()
        while prefptr[m] < len(pref[m]):
            w = pref[m][prefptr[m]]
            prefptr[m] += 1

            # skip blocked matches
            if (m, w) in blocked_set:
                continue

            if w not in S:
                S[w] = m
                break
            else:
                mprime = S[w]
                if rank[w][m] < rank[w][mprime]:
                    S[w] = m
                    freemen.add(mprime)
                    break
                else:
                    continue
    return S #return matches

def gs_tie(men, women, preftie):
    """
    Gale-Shapley algorithm modified to handle ties in preferences without flattening.
    
    Inputs:
        men (list): List of men's names.
        women (list): List of women's names.
        preftie (dict): Dictionary mapping each person to a list of sets,
                        where each set contains equally ranked partners.
    
    Output:
        dict: Stable matches as a dictionary mapping women to men.
    """
    # build rank dictionary
    rank = {}
    for w in women:
        rank[w] = {}
        for i, tier in enumerate(preftie[w]):
            for m in tier:
                rank[w][m] = i  # lower index = higher preference

    # track proposals and their ranking
    proposal_state = {m: [0, set()] for m in men}
    freemen = set(men)
    S = {}  

    # run the alogorithm
    while freemen:
        m = freemen.pop()
        tier_index, proposed_set = proposal_state[m]

        # go to next preference if current preference is engaged
        while tier_index < len(preftie[m]) and proposed_set == preftie[m][tier_index]:
            tier_index += 1
            proposed_set = set()
            proposal_state[m] = [tier_index, proposed_set]

        if tier_index >= len(preftie[m]):
            continue  # no more women to propose to

        # propose to one woman in current rank that isn't matched
        for w in preftie[m][tier_index]:
            if w not in proposed_set:
                proposed_set.add(w)
                proposal_state[m][1] = proposed_set

                if w not in S:
                    S[w] = m
                    break
                else:
                    mprime = S[w]
                    if rank[w][m] < rank[w][mprime]:
                        S[w] = m
                        freemen.add(mprime)
                        break
                    else:
                        freemen.add(m)
                        break

    return S  

if __name__=="__main__":
    #input data
    themen = ['xavier','yancey','zeus']
    thewomen = ['amy','bertha','clare']

    thepref = {'xavier': ['amy','bertha','clare'],
           'yancey': ['bertha','amy','clare'],
           'zeus': ['amy','bertha','clare'],
           'amy': ['yancey','xavier','zeus'],
           'bertha': ['xavier','yancey','zeus'],
           'clare': ['xavier','yancey','zeus']
           }
    thepreftie = {'xavier': [{'bertha'},{'amy'},{'clare'}],
           'yancey': [{'amy','bertha'},{'clare'}],
           'zeus': [{'amy'},{'bertha','clare'}],
           'amy': [{'zeus','xavier','yancey'}],
           'bertha': [{'zeus'},{'xavier'},{'yancey'},],
           'clare': [{'xavier','yancey'},{'zeus'}]
           }
    
    blocked = {('xavier','clare'),('zeus','clare'),('zeus','amy')}

    #eng
    match = gs(themen,thewomen,thepref)
    print(match)

    match_block = gs_block(themen,thewomen,thepref,blocked)
    print(match_block)

    match_tie = gs_tie(themen,thewomen,thepreftie)
    print(match_tie)
