class Trie:
    __slots__ = ('children', 'word')
    def __init__(self):
        self.children = {}
        self.word = True

def insert(root: Trie, s: str):
    curr = root
    for c in s:
        if c not in curr.children:
            curr.children[c] = Trie()
        curr = curr.children[c]
    curr.word = True

def search(root: Trie, s: str) -> bool:
    curr = root
    for c in s:
        if c not in curr.children:
            return False
        curr = curr.children[c]
    return curr.word
