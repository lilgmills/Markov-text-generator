##opens a SampleText file, and creates pairs of words that occur, and then a dictionary of opening words mapped to their list of following words

import os
import numpy as np

def makepairs(sample):
    for i in range(len(sample)-1):
        yield (sample[i], sample[i+1])
        
        ##the -2 range leaves off the \n entry, and leaves a
        ##buffer position for creating pairs

def decode(string):
    pass
    ##returns a string of 

def main():
    new_file = open("chain_words.txt", "w+")

    with open("speeches.txt", "r", encoding = "utf-8") as file_text:
        paragraphs = file_text.read().split("\n")
        
        ##creates paragraphs as a list of strings by splitting on spaces

    paragraphs_lists = [para.split(" ") for para in paragraphs]
    ##turns a list of paragraphs into a list of word lists
    listwords = []
    for list in paragraphs_lists:
        listwords += list

        ##finishes putting paragraphs into list form
        

    #for i in range(len(listwords)):
     #   print(listwords[i])
            
        
    pairs = makepairs(listwords)

    word_dict = {}

    for word1, word2 in pairs:
        if word1 in word_dict.keys():
            word_dict[word1].append(word2)
        else:
            word_dict[word1] = [word2]

        ##puts each opener word in a dictionary if it isn't already there

    for key in word_dict.keys():
        try:
            new_file.write(key + ':' +'[' + ', '.join(word_dict[key]) + ']' +'\n')
        except:
            if key:
                print(word_dict[key])
    ##create word dictionary string to go into a file

    new_file.close()

    first_word = np.random.choice(listwords)
    while first_word.islower():
        first_word = np.random.choice(listwords)

    chain = [first_word]

    num_words = 400

    for i in range (num_words):
        chain.append(np.random.choice(word_dict[chain[-1]]))
    with open("newSpeechScript.txt", "w+") as f:
        print(' '.join(chain) , file =f)


filepath = "C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python38-32\\Environment\\python poem"
os.chdir(filepath)

if __name__ == "__main__":
    main()
    
    
