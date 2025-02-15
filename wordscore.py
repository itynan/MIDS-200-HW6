from itertools import chain, combinations


def score_word(words):
    '''Takes in a list and returns a tuple of tuples(including the count of tuples that each contain a word and a score). Each character in each word 
    in words(list) is evaluated for its character score and that score is aggregated and stored in a tuple next to the word evaluated (5,'MAT')
    into scabble.py
    '''
    output = []

    for word in words:
        output.append(output_tpl_bldr(word))
    
    return output, len(output)

def output_tpl_bldr(word):
    
    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
        "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
        "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
        "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
        "x": 8, "z": 10}


    before_count = (sum(scores.get(char.lower(), 0) for char in word))        
    add_count =(before_count, word) 
    return add_count 



#TODO:FIGURE OUT WHAT TO DO WITH CASES IN TERMS OF INPUT AND SCORES DICT - 
# DONE convert lower for char count when evaluating against scores dictionary score

#taken from lecture 6.2.2, func returns the powerset of a word's characters
def powerset(iterable):
    if(type(iterable) != str or len(iterable) < 2 or len(iterable) > 7):
        raise TypeError("Input must be string with more than one character")
    else:
        iterable = tuple(iterable.upper())
        s = list(iterable)
        all_tuples= list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
            
        #for loop constructs list of all possible permutations into contiguous words and removes tuples with <2 chars and > 7
        words_to_check = []
        for tupl in all_tuples:
            word = "".join(tupl) 
            #run redundant checks 
            if(len(word) > 1 and len(word) < 8):
                words_to_check.append(word)
        return words_to_check
    

#print(powerset("HAT"))