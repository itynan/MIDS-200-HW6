from itertools import chain, permutations

perm_memo = {}

def score_word(words,orig_count):
    '''Takes in a list and returns a tuple of tuples(including the count of tuples that each contain a word and a score). Each character in each word 
    in words(list) is evaluated for its character score and that score is aggregated and stored in a tuple next to the word evaluated (5,'MAT')
    into scabble.py
    '''
    output = []
    for word in words:
        output.append(output_tpl_bldr(word,orig_count))
    #https://stackoverflow.com/questions/3121979/how-to-sort-a-list-tuple-of-lists-tuples-by-the-element-at-a-given-index
    #this lambda sorts first by descending(NEGATIVE) numbers -x[0] and then alpha order
    sorted_num_alpha = sorted(output, key=lambda x: (-x[0], x[1]))
    return sorted_num_alpha, len(sorted_num_alpha)



#TODO:FIGURE OUT WHAT TO DO WITH CASES IN TERMS OF INPUT AND SCORES DICT - 
# DONE convert lower for char count when evaluating against scores dictionary score
def gen_perms(iterable):
    if iterable in perm_memo:
        return perm_memo[iterable]

    words_to_check = set()

    for perm in range(2, min(len(iterable)+ 1, 8)):
        perms = {"".join(tupl) for tupl in permutations(iterable,perm)}
        perm_memo[(iterable,perm)] = perms
        words_to_check.update(perms)

    perm_memo[iterable] = words_to_check
    return words_to_check


#taken from lecture 6.2.2, func returns the powerset of a word's characters
def powerset(iterable):
    #https://www.geeksforgeeks.org/python-itertools-product/


    try:
        iterable = iterable.upper()
        wc_count = iterable.count("*") + iterable.count("?")

        wc_element = [x for x, c in enumerate(iterable) if c in "*?"]

        wc_case = [[],0]
        if len(iterable) == 2 and wc_count == 2:
            return wc_case

        if wc_count == 0:
            words_to_check = gen_perms(iterable)
            return list(words_to_check)

        words_to_check = set()
        
        strip_wc = "".join(x if x not in "*?" else "_" for x in iterable)
        memo_base = gen_perms(strip_wc.replace("_",""))

        words_to_check = set()
        non_wc_vals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        perm_memo_key = (strip_wc, wc_count, tuple(wc_element))
        if perm_memo_key in perm_memo:
            return list(perm_memo[perm_memo_key])
        
        combination_set = set() 
        #address edge case where there is only 1 char and only 1 wildcard
        if wc_count == 1 and (len(iterable) == 2):
            if iterable[0] not in "*?":
                for letter in non_wc_vals:
                    combination_set.add(iterable[0]+letter)
            else:
                for letter in non_wc_vals:
                    combination_set.add(letter+iterable[1])

            return list(combination_set)
        if wc_count == 1:
            #perm_memo_key = (strip_wc, 1, tuple(wc_element))
            wc = wc_element[0] 
            wc1_words = set()
            words_to_check = gen_perms(iterable)
            for word in memo_base:
                for char in non_wc_vals:
                    new_word = word[:wc] +char +word[wc+1:]
                    wc1_words.add(new_word)
            return list(wc1_words)

            # if perm_memo_key in perm_memo:
            #     return list(perm_memo[perm_memo_key])
            

        if wc_count == 2:
            pass
        
    except Exception as e:
        print("Error:", e)
        return []
        

#print(powerset("HAT"))

def output_tpl_bldr(word, orig_count):
    '''function aggregates all scores per word and adds the value 
    in front of the word in a tuple to be added to the large output tuple
    appends the final tuple with the total count of words'''
    

    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
        "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
        "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
        "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
        "x": 8, "z": 10}
    
    minus_wc = dict(orig_count)
    letter_score = 0
   
    for char in word:
        #if char is to be counted, perform lookup in scores and add its value to letter_score
        #then remove it from minus_wc
        if minus_wc.get(char.lower(), 0) > 0:
            #print(char)
            letter_score += scores.get(char.lower(), 0)
            minus_wc[char.lower()] -= 1
            #print(minus_wc)

    return (letter_score,word)

    # before_count = (sum(scores.get(char.lower(), 0) for char in word))        
    # add_count =(before_count, word) 
    # return add_count
