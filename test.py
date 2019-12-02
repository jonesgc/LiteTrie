import liteTrie

def main():
    trie = liteTrie.createTrie("test")
    liteTrie.printTrie(trie)
    liteTrie.addNewWord(trie, "Hello")
    liteTrie.addNewWord(trie, "Melm")
    liteTrie.printTrie(trie)


if __name__ == "__main__":
    main()