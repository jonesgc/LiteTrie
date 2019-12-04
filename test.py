import liteTrie

def main():
    trie = liteTrie.createTrie("test")
    liteTrie.addNewWord(trie, "Hello")
    liteTrie.addNewWord(trie, "Melm")
    liteTrie.addNewWord(trie, "tea")
    liteTrie.printTrie(trie)
    
    inputWord = input("Enter a letter to find a predicted word: ")
    print("Entered letter was t")

    suggestions = liteTrie.findWord(trie , inputWord)
    print(suggestions)
    
if __name__ == "__main__":
    main()
