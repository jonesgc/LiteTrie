import liteTrie

def main():
    trie = liteTrie.createTrie("test")
    liteTrie.addNewWord(trie, "Hello")
    liteTrie.addNewWord(trie, "Melm")
    liteTrie.addNewWord(trie, "tea")
    liteTrie.printTrie(trie)
    
    inputSequence = input("Enter a sequence to find a predicted word: ")
    print("Entered sequence was:", inputSequence)

    suggestions = liteTrie.findWord(trie , inputSequence)
    print(suggestions)
    
if __name__ == "__main__":
    main()
