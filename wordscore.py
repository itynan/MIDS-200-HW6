from itertools import chain, combinations


#will take each word and return the score to be imported into scabble.py
def score_word(words):

    output = []

    for word in words:
        output.append(output_tpl_bldr(word))
    
    return output

def output_tpl_bldr(word):
    
    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
        "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
        "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
        "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
        "x": 8, "z": 10}


    return (word, sum(scores.get(char.lower(), 0) for char in word))          

#aggreagte word score
#TODO: aggregfate score per char and construct tuple list



    
    return scores




#TODO:FIGURE OUT WHAT TO DO WITH CASES IN TERMS OF INPUT AND SCORES DICT

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