# pytest 4.6.6 test file for liteTrie.py

import liteTrie
import ezPyQueue

# Test if the addleaf function creates a liteTrie node object.
def test_addLeaf():
    tc = "T"
    test_Trie = liteTrie.node("T")
    test_Trie.addLeaf(tc)
    assert test_Trie.leaf > 1

# Test if the createTrie function creates a liteTrie node object.
def test_createTrie():
    tc = "TESTCASE"
    result = liteTrie.createTrie("TESTCASE")
    assert isinstance(result, liteTrie.node)

# Basic add word test that counts the number of leaves, created with a testcase and compares them to a predetermined value.
# Some basic code for this test come from the liteTrie.printTrie(trie) function
def test_basic_addWord():
    target = 5 # target is 5 since we will count the root node in addition to the testcase.
    tc = "TEST"
    trie = liteTrie.createTrie(tc)

    leafCounter = 0

    q = ezPyQueue.ezQueue()
    q.place(trie)

    while q.isEmpty() == False:
        node = q.popTop()
        leafCounter = leafCounter + 1

        # Add leaves to queue.
        if not node.leaf:
            print("End of word")
        for l in node.leaf:
            q.place(l)

    assert leafCounter == target