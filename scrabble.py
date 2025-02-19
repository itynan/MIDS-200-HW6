from collections import defaultdict
from wordscore import score_word, powerset

def orig_word_count(p_word):
    '''method counts how many times a char is seen in a 
    word to help you keep track of the word's score''' 
    orig_count = {}
    for char in p_word:
        if char not in "?*":
            c = char.lower()
            orig_count[c] = orig_count.get(c, 0) + 1

    return orig_count
def create_word_dict():
    '''key should be two letters since only 2 letter words and larger are used
    https://www.geeksforgeeks.org/defaultdict-in-python/?utm_source=chatgpt.com
    using default dict to create a dictionary of dictionaries organized by first 
    two letters EX: {"AA": "AA","AARDVARK" } etc'''
    
    try:
        with open("sowpods.txt","r") as infile:
            raw_input = infile.readlines()
    except IOError:
        raise IOError("ERROR reading file")
        
    data = [datum.strip('\n') for datum in raw_input]
    if not data:
        raise ValueError("File missing words to parse")

    #two pointer approach to populate dict more efficiently 
    left = 0
    right = len(data) - 1
    mid = len(data) // 2
    
    word_dict = defaultdict(list)

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

    
    if len(p_word) == 2 and ((p_word.count("*") + p_word.count("?"))==2):
        print(wc_case)
        return[list([]),0]
    
    
    if any(char.isdigit() for char in p_word):
        return "Input must contain NO numbers"
    
    if any(char not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz?*" for char in p_word):
        return "Input must contain no non alpha chars; 1 or 2 wildcard chars are ok: * + ? "

    if not isinstance(p_word, str):
        return "Input must be string with more than one character"
    if len(p_word) < 2:
         return "Error: Input must be string with more than one character"
    if len(p_word) > 7:
        return "Error: Input must be string with less than 8 chars"
    if p_word.count("*") + p_word.count("?") > 2:
        return "Input contains more than 2 wildcards"


    word_dict = create_word_dict()
    
    words_to_check = powerset(p_word)
    
    list_to_score = []
    for word in words_to_check:
        first_two = [word[:2]] if "?" not in word and "*" not in word else [letter + word[1] for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]

        for ft in first_two:
            sub_dict = word_dict.get(ft, [])
            if word in sub_dict and word not in list_to_score:
                list_to_score.append(word)

    # print(list_to_score)
    orig_count = orig_word_count(p_word)
    
    output = score_word(list_to_score, orig_count)
    #print(f"output from score_word = {output}") 

    print(output)

    return output
if __name__ == "__main__":
    run_scrabble("?*")
   

