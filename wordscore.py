from itertools import combinations, permutations
from collections import defaultdict


powerset_memo = {}

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

def powerset(iterate):

    if iterate in powerset_memo:
        return powerset_memo[iterate]

    chars = list(iterate)
    length = len(chars)

    output = set()

    for ele in range(2, min(7,length) + 1):
        for comb in combinations(chars, ele):
            wc_count = comb.count('?') + comb.count('*') 
            for perm in permutations(comb):
                if wc_count == 0:
                    for perm in permutations(comb):
                        output.add("".join(perm))

                if wc_count == 1:
                    for sub in one_wc(perm):
                        output.add("".join(sub))
                if wc_count == 2:
                    for sub in two_wcs(perm):
                        output.add("".join(sub))

    output = list(output)
    powerset_memo[iterate] = output
    return output

def one_wc(comb):
    results = []
    non_wc_vals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    comb_list = list(comb)
    index = 0

    for x, char in enumerate(comb_list):
        if char in ('?',"*"):
            index = x
            break
    for x in non_wc_vals:
        all_chars_list = comb_list[:]
        all_chars_list[index] = x
        results.append(tuple(all_chars_list))
    return results

def two_wcs(comb):
    results = []
    non_wc_vals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    comb_list = list(comb)
    wc_index = [i for i, char in enumerate(comb_list) if char in ('?',"*")]
    wc1 = wc_index[0]
    wc2 = wc_index[1]

    for let1 in non_wc_vals:
        for let2 in non_wc_vals:
            all_chars_list = comb_list[:]
            all_chars_list[wc1] = let1
            all_chars_list[wc2] = let2
            results.append(tuple(all_chars_list))
    return results