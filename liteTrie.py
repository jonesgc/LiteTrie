#liteTrie is my experimentation with tries in pyhton.
# Using pytest-4.6.6 
import ezPyQueue

#Char should be the letter that is the "payload"
#Leaves will be a list of leaf nodes that will branch off from a parent node.
class node:
    def __init__(self, char):
        self.payload = char
        self.leaf = []

#Add a leaf to the node, the leaves are stored in a list of node objects.
    def addLeaf(self, char):
        newLeaf = node(char)
        self.leaf.append(newLeaf)
        print("New leaf created with payload of:", char)
        return newLeaf


#Creates the trie with a starting word, the root node is blank, the end nodes of a breanch will have a payload but they will have no leaves.
def createTrie(word):
    #Create blank root node
    root = node("ROOT")
    print("Created ROOT")
    i = len(word)
    print(i)
    current = root
    for x in range (0, i):
        new = current.addLeaf(word[x])
        current = new
        x = x+1

    return root


#Prints the current payloads of the leaves attached to the current node.
def printLeavesOnCur(cur):
    numberOfleaves = len(cur.leaf)
    print("---" * numberOfleaves)
    for l in cur.leaf:
        print(l.payload)

#Prints the entire trie.
def printTrie(trie):
    #Print the current node (this would normally be the root node).
    #Create a queue of leaves that need to be printed at the root level.
    q = ezPyQueue.ezQueue()
    q.place(trie)
    print(type(trie))
        
        
    while q.isEmpty() == False:
        node = q.popTop()
        print(node.payload)

        # Add leaves to queue.
        if not node.leaf:
            print("End of word")
        for l in node.leaf:
            q.place(l)
            

#Add a new word to the root node, checking to see if it shares the starting letter with any current entries.
# -- TO DO -- Need to check if the word has already been added i.e. all the letters are already in the trie in the same order.
def addNewWord(root, word):
    i = len(word)

    testFlag = False
    for node in root.leaf:
        
        if word[0] == node.payload:
            print("Matching start letter found.")
            testFlag = True
            current = node

            # Note here that the for loop starts at 1 meaning it does not add the duplicate letter.
            for x in range (1, i):
                new = current.addLeaf(word[x])
                current = new
                x = x+1


    if testFlag == False:
        print("Starting letters do not match, creating new branch")
        current = root
        for x in range (0, i):
            new = current.addLeaf(word[x])
            current = new
            x = x+1

# Find Word function compares a input sequence of letters againsts the trie and returns possible matches.
def findWord(root, sequence):
    suggestions = []
    suggestWord = 0
    depth = 0

    for rootLeaf in root.leaf:

        # Matched the starting letter of a word to that of the sequence.
        if sequence[0] == rootLeaf:
            suggestWord = suggestWord + sequence[0]
            
            return suggestions
            
        else:
            print("No matches based on entered sequence.")

            return False


    
    

    
    
