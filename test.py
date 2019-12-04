import liteTrie

def main():
    trie = liteTrie.createTrie("test")
    liteTrie.addNewWord(trie, "Hello")
    liteTrie.addNewWord(trie, "Melm")
    liteTrie.addNewWord(trie, "tea")
    liteTrie.printTrie(trie)
    
if __name__ == "__main__":
    main()
