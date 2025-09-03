# Caroline Briggs
# Python implementation of stable matching problem
# Homework 1 Starter Code
# CYB 2013

def gs(men, women, pref):
    # Step 1: Create a dictionary to track who each woman prefers more
    rank = {}
    for woman in women:
        rank[woman] = {}
        for i in range(len(pref[woman])):
            man = pref[woman][i]
            rank[woman][man] = i  # Lower index means higher preference

    # Step 2: Track which woman each man will propose to next
    next_choice = {}
    for man in men:
        next_choice[man] = 0  # Start at the top of his list

    # Step 3: Keep track of free men and current engagements
    freemen = men[:]
    engagements = {}  # woman → man

    # Step 4: Repeat until all men are matched
    while freemen:
        man = freemen.pop(0)  # Take the first free man
        woman = pref[man][next_choice[man]]  # Get his next top choice
        next_choice[man] += 1  # Move to the next woman for future proposals

        if woman not in engagements:
            # She's free, so they get engaged
            engagements[woman] = man
        else:
            current = engagements[woman]
            # Check if she prefers the new man over her current one
            if rank[woman][man] < rank[woman][current]:
                # She prefers the new man
                engagements[woman] = man
                freemen.append(current)  # The old fiancé becomes free again
            else:
                # She stays with her current match
                freemen.append(man)

    # Step 5: Flip the engagements to man → woman format
    match = {}
    for woman in engagements:
        man = engagements[woman]
        match[man] = woman

    return match

def gs_block(men, women, pref, blocked):
    # Initialize all men and women as free
    freemen = men[:]
    engaged = {}
    proposals = {man: [] for man in men}

    # Create a quick lookup for blocked pairs
    blocked_set = set(blocked)

    while freemen:
        man = freemen.pop(0)
        man_pref = pref[man]

        # Propose to the next woman on his list who hasn't been proposed to yet
        for woman in man_pref:
            if woman in proposals[man] or (man, woman) in blocked_set:
                continue

            proposals[man].append(woman)

            if woman not in engaged:
                # She's free, engage them
                engaged[woman] = man
                break
            else:
                current_man = engaged[woman]
                woman_pref = pref[woman]

                # Check if she prefers this new man over her current engagement
                if woman_pref.index(man) < woman_pref.index(current_man):
                    # She prefers the new man
                    engaged[woman] = man
                    freemen.append(current_man)
                    break
                else:
                    # She stays with her current partner
                    continue

    # Convert engaged dict to man -> woman format
    return {man: woman for woman, man in engaged.items()}

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
    
    #match_block = gs_block(themen,thewomen,thepref,blocked)
   # print(match_block)

    #match_tie = gs_tie(themen,thewomen,thepreftie)
   # print(match_tie)
