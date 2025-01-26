
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class EndOfWordTrieNode(TrieNode):
    def __init__(self):
        super().__init__()
        self.is_end_of_word = True
        self.data = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, data):
        current = self.root
        for i in range(len(word)):
            letter = word[i]
            if letter not in current.children:
                if i == len(word) - 1:
                    current.children[letter] = EndOfWordTrieNode()
                    current.children[letter].data.append(data)
                else:
                    current.children[letter] = TrieNode()
            current = current.children[letter]

    def search(self, word):
        current = self.root
        for i in range(len(word)):
            letter = word[i]
            if letter not in current.children:
                return None
            current = current.children[letter]

        # from current, traverse all children and return the data
        visited = set()
        visited.add(current)
        stack = [current]
        matches = []
        while len(stack) > 0:
            node = stack.pop()
            if node.is_end_of_word:
                matches.extend(node.data)
            for child in node.children.values():
                if child not in visited:
                    stack.append(child)
                    visited.add(child)

        return matches
