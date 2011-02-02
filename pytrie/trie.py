

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.value = None


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def __len__(self):
        pass

    def __getitem__(self, key):
        node = self.root
        for char in key:
            if char in node.children:
                node = node.children[char]
            else:
                raise KeyError('key %s not in trie' % key)
        return node.value

    def __setitem__(self, key, value):
        if not len(key):
            raise ValueError('key must be non-empty')
        
        node = self.root
        for char in key:
            if char in node.children:
                node = node.children[char]
            else:
                node.children[char] = TrieNode()

        node.value = value

    def __delitem__(self, key):
        pass

    def __iter__(self):
        pass

    def __contains__(self, key):
        pass
