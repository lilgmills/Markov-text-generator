"""opens a SampleText file, and creates pairs of words that occur,
and then a markov dictionary which is used to generate sample words with appropriate frequencies
"""

import os
from random import choice

def listfromsample(sample_file):
    """
    puts a sample of text into a list of words (with punctuation) from start to finish
    """
    with open(sample_file, "r", encoding = "utf-8") as sample_text:
        paragraphs = sample_text.read().split("\n")
        
        ##creates paragraphs as a list of strings by splitting on line breaks

    paragraph_iter = filter(not_empty, paragraphs)

    paragraphs_lists = [para.split(" ") for para in paragraph_iter]
    ##turns a list of paragraphs into a list of word lists
    
    listwords = []
    for list in paragraphs_lists:
        listwords += list

        ##finishes putting paragraphs into list form

    return listwords

def makepairs(sample_list):
    for i in range(len(sample_list)-1):
        yield (sample_list[i], sample_list[i+1])

def make3gram(list_words):
    for i in range(len(list_words) -2):
        yield (list_words[i], list_words[i+1], list_words[i+2])

def markov_pairs_dict(iterable_pairs):
    word_dict = {}
    for word1, word2 in iterable_pairs:                
        if word1 in word_dict.keys():
            word_dict[word1].append(word2)
        else:
            word_dict[word1] = [word2]

        ##puts each opener word in a dictionary if it isn't already there

    return word_dict

def markov_trigram_dict(iterable_trigrams):
    tri_dict = {}
    for word1, word2, word3 in iterable_trigrams:
        if (word1, word2) in tri_dict.keys():
            tri_dict[(word1, word2)].append(word3)
        else:
            tri_dict[(word1, word2)] = [word3]

    return tri_dict

def create_chain_text(tri_dict, num = 60):
    """
    Generates a segment of text of a given length from a dictionary of trigram frequencies
    """
    trikeylist = list(tri_dict.keys())
    starter_pairs = list(filter(starter_pair, trikeylist))

    chain = [choice(starter_pairs)]

    for i in range(num):
        selection = choice(tri_dict[chain[-1]])
        chain.append((chain[-1][1], selection))

    chain_words = [chain[0][0]]
    for x, y in chain:
        chain_words.append(y)
        if y:
            if y[-1] == ".":
                end_word = len(chain_words)
            ##finding the last period in the text sample
    try:
        chain_words = chain_words[:end_word]
    except:
        pass

    return chain_words

def not_empty(string):
    return not string == ''

def starter_pair(tup):
    return not tup[0].islower() and len(tup[0]) > 1

def quit(default = ""):
    return default == "exit" or default == "quit"    

def decode(string):
    pass
    """
    if needed, a function to prepare encoding and formatting of individual words
    """

def Display(tri_dict):
    new_default = input('\nPress Enter or type length of sample (default 40) (type "exit" to exit): ')    
    try:
        new_default = int(new_default)
    except:
        pass
    if not quit(new_default):
        if isinstance(new_default, int):
            chain_words = create_chain_text(tri_dict, new_default)
        else:
            chain_words = create_chain_text(tri_dict)

        print(' '.join(chain_words))

    return new_default
    

def main(default = True):
    sample_file = "speeches.txt"         
    listwords = listfromsample(sample_file)    
    tris = make3gram(listwords)
    tri_dict = markov_trigram_dict(tris)

    while not quit(default):
        default = Display(tri_dict)

    

if __name__ == "__main__":
    main()
    
    
