"""opens a SampleText file, and creates pairs of words that occur,
and then a markov dictionary which is used to generate sample words with appropriate frequencies
"""

import os
from random import choice

def not_empty(string):
    return not string == ''

def starter_pair(tup):
    return not tup[0].islower()

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
    

def decode(string):
    pass
    """
    if needed, a function to prepare encoding and formatting of individual words
    """


def main():
    sample_file = "speeches.txt"         
    listwords = listfromsample(sample_file)    
    tris = make3gram(listwords)

    tri_dict = markov_trigram_dict(tris)

    num = 180

    trikeylist = list(tri_dict.keys())
    starter_pairs = list(filter(starter_pair, trikeylist))

    chain = [choice(starter_pairs)]

    for i in range(num):
        selection = choice(tri_dict[chain[-1]])
        chain.append((chain[-1][1], selection))

    chain_words = [chain[0][0]]
    for x, y in chain:
        chain_words.append(y)

    with open(f"NewScript{num}.txt", "w+") as f:
        print(' '.join(chain_words), file =f)    
    

    

if __name__ == "__main__":
    main()
    
    
