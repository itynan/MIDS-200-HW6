from collections import defaultdict
from wordscore import score_word, powerset

def create_word_dict():
    with open("sowpods.txt","r") as infile:
        raw_input = infile.readlines()
        data = [datum.strip('\n') for datum in raw_input]
    

    #two pointer approach to populate dict more efficiently 
    left = 0
    right = len(data) - 1
    mid = len(data) // 2
    
    word_dict = defaultdict(list)

    '''key should be two letters since only 2 letter words and larger are used
    https://www.geeksforgeeks.org/defaultdict-in-python/?utm_source=chatgpt.com
    using default dict to create a dictionary of dictionaries organized by first 
    two letters EX: {"AA": "AA","AARDVARK" } etc'''

    while left <= mid and right > mid:
        for i in [left,right]:
            if(len(data[i])) >= 2 and (len(data[i])) < 8:
                
                d_key = data[i][:2]
                word_dict[d_key].append(data[i])
        left += 1
        right -= 1

    return word_dict

def run_scrabble(p_word):
    '''This is the main function that first validates the word input for a proper input string, then
    passes the the word into a powerset function that generates a list of all possible permutations.
    All permutations are tested against a dictionary of real words provided  '''


    if not isinstance(p_word, str) or len(p_word) < 2:
        raise TypeError("Input must be string with more than one character")
    if len(p_word) > 7:
                return "Error: Input must be string with more than one character"

    if p_word.count("*") + p_word.count("?") > 2:
        raise TypeError("Input contains more than 2 wildcards")


    
    word_dict = create_word_dict()
    
    words_to_check = powerset(p_word)
    list_to_score = []
    for word in words_to_check:
        sub_dict = word_dict.get(word[:2],[])
        if word in sub_dict and word not in list_to_score:
            list_to_score.append(word)
    #print(list_to_score)
    output = score_word(list_to_score)
    
    print(output)
    return output
if __name__ == "__main__":
    run_scrabble("AB")
   