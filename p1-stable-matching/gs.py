# Caroline Briggs
# Python implementation of stable matching problem
# Homework 1 Starter Code
# CYB 2013

def gs(men, women, pref):
    rank = {}
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
    # Step 1: Build ranking dictionary for women
    rank = {w: {m: i for i, m in enumerate(pref[w])} for w in women}
  
    # Step 2: Track which woman each man will propose to next
    prefptr = {m: 0 for m in men}

    # Step 3: Track free men and current engagements
    freemen = set(men)
    S = {}  # woman → man
    blocked_set = set(blocked)

    # Step 4: Run the matching loop
    while freemen:
        m = freemen.pop()
        while prefptr[m] < len(pref[m]):
            w = pref[m][prefptr[m]]
            prefptr[m] += 1

            # Skip blocked pairs
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

    # Step 5: Convert woman → man to man → woman
    return {w: m for w, m in S.items()}

def gs_tie(men, women, preftie):
    # Flatten tied preferences into ordered lists for proposal tracking
    def flatten(pref_list):
        return [name for group in pref_list for name in sorted(group)]

    # Build flattened preference lists
    flat_pref = {person: flatten(preftie[person]) for person in preftie}

    # Initialize proposal tracking
    free_men = men[:]
    proposals = {man: [] for man in men}
    engagements = {}

    while free_men:
        man = free_men.pop(0)
        for woman in flat_pref[man]:
            if woman in proposals[man]:
                continue
            proposals[man].append(woman)

            if woman not in engagements:
                engagements[woman] = man
                break
            else:
                current_man = engagements[woman]
                woman_flat = flat_pref[woman]

                # Compare positions in flattened preference list
                if woman_flat.index(man) < woman_flat.index(current_man):
                    engagements[woman] = man
                    free_men.append(current_man)
                    break
                else:
                    continue

    return {man: woman for woman, man in engagements.items()}

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

    #match_tie = gs_tie(themen,thewomen,thepreftie)
   # print(match_tie)
