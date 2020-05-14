"""
Week 2, Day 7: Implement Trie (Prefix Tree)

Implement a trie with insert, search, and startsWith methods.

E x a m p l e

    Trie trie = new Trie();

    trie.insert("apple");
    trie.search("apple");   // returns true
    trie.search("app");     // returns false
    trie.startsWith("app"); // returns true
    trie.insert("app");
    trie.search("app");     // returns true

N o t e

    - You may assume that all inputs are consist of lowercase letters a-z.
    - All inputs are guaranteed to be non-empty strings.

A P I   U s a g e

    Your Trie object will be instantiated and called as such:

        obj = Trie()
        obj.insert(word)
        param_2 = obj.search(word)
        param_3 = obj.startsWith(prefix)
"""


class Trie:

    def __init__(self):
        self.trie = dict()

    def insert(self, word: str) -> None:
        """ Inserts a word into the trie. """
        current = self.trie
        for ch in word:
            if ch not in current:
                current[ch] = dict()
            current = current[ch]
        current['*'] = True

    def _search(self, word: str):
        current = self.trie
        for ch in word:
            if ch not in current:
                return {}
            current = current[ch]
        return current

    def search(self, word: str) -> bool:
        """ Returns if the word is in the trie. """
        return '*' in self._search(word)

    def startsWith(self, prefix: str) -> bool:
        """ Returns if there is any word in the trie that starts with the given prefix. """
        return self._search(prefix) != {}


if __name__ == '__main__':
    obj = Trie()
    obj.insert('apple')
    print(obj.search('apple') is True)
    obj.insert('hi')
    obj.insert('hello')
    print(obj.search('app') is False)
    print(obj.startsWith('app') is True)
    obj.insert('app')
    print(obj.search('app') is True)
    print(obj.search('hi') is True)
    print(obj.search('hello') is True)
    obj.insert('leetcode')
    print(obj.search('leet') is False)
    print(obj.search('code') is False)
    print(obj.search('leetcode') is True)
    print(obj.startsWith('leet') is True)
    print(obj.startsWith('h') is True)

# last line of code
