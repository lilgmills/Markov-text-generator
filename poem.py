"""
opens a SampleText file, and creates trigrams of words that occur,
and then a markov dictionary which is used to generate sample words with appropriate frequencies
"""

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

def make3gram(list_words):
    for i in range(len(list_words) -2):
        yield (list_words[i], list_words[i+1], list_words[i+2])

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

def decode(string):
    pass
    """
    if needed, a function to prepare encoding and formatting of individual words
    """

class DisplayChain():
    
    def __init__(self, tri_dict, interpreter = True):
        self.tri_dict = tri_dict
        self.interpreter = interpreter
        self.sessionID = 0
        self.new_default = ""

    def quit(self, default = ""):
        return default == "exit" or default == "quit"
        
    def mainloop(self):
        self.new_default = input('\nPress Enter or type length of sample (default 60) (type "exit" to exit): ')
        if not self.quit(self.new_default):
            try: self.new_default = int(self.new_default)
            except: pass
            
            if isinstance(self.new_default, int):    
                self.chain_words = create_chain_text(self.tri_dict, self.new_default)
            else:
                self.chain_words = create_chain_text(self.tri_dict)

            if self.interpreter:
                print(' '.join(self.chain_words))
            else:
                with open(f"newoutput{self.sessionID}.txt", "w+") as f:
                    print(' '.join(self.chain_words), file =f)
                print(f'outputted to newoutput{self.sessionID}.txt')
                self.sessionID+=1

    
def main():
    
    sample_file = "speeches.txt"
    
    listwords = listfromsample(sample_file)    
    tris = make3gram(listwords)
    tri_dict = markov_trigram_dict(tris)
    
    f = DisplayChain(tri_dict)
    while not f.quit(f.new_default):
        f.mainloop()
    
    
if __name__ == "__main__":
    main()
    
    
