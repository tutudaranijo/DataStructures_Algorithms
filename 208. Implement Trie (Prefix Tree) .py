class TrieNode:
    def __init__(self):  # constructor
        self.children = {}
        self.endOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()  # initialize this , empty to start

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:  # not in hash map create a try node for it
                cur.children[c] = TrieNode()  # inserting node
            cur = cur.children[c]
        cur.endOfWord = True  # then mark it as the end of the word

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:  # word doesn't exist
                return False
            cur = cur.children[c]
        return cur.endOfWord  # if word not there its gonna return false

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
