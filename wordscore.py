from itertools import chain, permutations

perm_memo = {}

def score_word(words):
    '''Takes in a list and returns a tuple of tuples(including the count of tuples that each contain a word and a score). Each character in each word 
    in words(list) is evaluated for its character score and that score is aggregated and stored in a tuple next to the word evaluated (5,'MAT')
    into scabble.py
    '''
    output = []

    for word in words:
        output.append(output_tpl_bldr(word))
    #https://stackoverflow.com/questions/3121979/how-to-sort-a-list-tuple-of-lists-tuples-by-the-element-at-a-given-index
    #this lambda sorts first by descending(NEGATIVE) numbers -x[0] and then alpha order
    sorted_num_alpha = sorted(output, key=lambda x: (-x[0], x[1]))
    return sorted_num_alpha, len(sorted_num_alpha)



#TODO:FIGURE OUT WHAT TO DO WITH CASES IN TERMS OF INPUT AND SCORES DICT - 
# DONE convert lower for char count when evaluating against scores dictionary score
def gen_perms(iterable):
    

    words_to_check = set()

    for perm in range(2, min(len(iterable)+ 1, 8)):
        if(iterable, perm) in perm_memo:
            words_to_check.update(perm_memo[(iterable,perm)])
        else:
            perms = {"".join(tupl) for tupl in permutations(iterable,perm)}
            perm_memo[(iterable,perm)] = perms
            words_to_check.update(perms)

    return words_to_check


#taken from lecture 6.2.2, func returns the powerset of a word's characters
def powerset(iterable):
    #https://www.geeksforgeeks.org/python-itertools-product/


    try:
        iterable = iterable.upper()
        wc_count = iterable.count("*") + iterable.count("?")

        wc_element = [x for x, c in enumerate(iterable) if c in "*?"]

        words_to_check = set()
        wc_vals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


        
        if wc_count == 0:
            words_to_check = gen_perms(iterable)
        
        
        
        
        

        if wc_count == 1:
            strip_wc = "".join(x  for x in iterable if x not in "*?")
            #perm_memo_key = (strip_wc, 1, tuple(wc_element))
            wc = wc_element[0] 
            wc1_words = set()
            words_to_check = gen_perms(iterable)
            for word in words_to_check:
                for chr in wc_vals:
                    new_word = word[:wc] +chr +word[wc:]
                    wc1_words.add(new_word)
            words_to_check = wc1_words
            words_to_check 

            # if perm_memo_key in perm_memo:
            #     return list(perm_memo[perm_memo_key])
            

        if wc_count == 2:
            pass

        return words_to_check
    except Exception as e:
        print("Error:", e)
        

#print(powerset("HAT"))

def output_tpl_bldr(word):
    '''function aggregates all scores per word and adds the value 
    in front of the word in a tuple to be added to the large output tuple
    appends the final tuple with the total count of words'''
    
    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
        "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
        "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
        "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
        "x": 8, "z": 10}


    before_count = (sum(scores.get(char.lower(), 0) for char in word))        
    add_count =(before_count, word) 
    return add_count 
