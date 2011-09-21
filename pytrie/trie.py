class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.value = None


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def __len__(self):
        def count(node):
            len = 0
            for char in node.children:
                if node.children[char].value:
                    len += 1
                len += count(node.children[char])
            return len

        return count(self.root)

    def __getitem__(self, key):
        node = self.root
        for char in key:
            if char in node.children:
                node = node.children[char]
            else:
                raise KeyError('key %s not in trie' % key)
        return node.value

    def __setitem__(self, key, value):
        if not key or not len(key):
            raise KeyError('key must be non-empty')
        
        node = self.root
        for char in key:
            if char in node.children:
                node = node.children[char]
            else:
                node.children[char] = node = TrieNode()

        node.value = value

    def __delitem__(self, key):
        parent_char = None
        node = parent = self.root
        for char in key:
            if char in node.children:
                if not len(node.children[char].children) and \
                   not node.children[char].value:
                    del node.children[char]
                parent_char = char
                parent = node
                node = node.children[char]
            else:
                raise KeyError('key does not exist')
        if node.value:
            del parent.children[parent_char]

    def __iter__(self):
        def preorder(node, path=''):
            for char in sorted(node.children):
                curpath = "%s%s" % (path, char)
                if node.children[char].value:
                    yield curpath
                for i in preorder(node.children[char], curpath):
                    yield i

        for i in preorder(self.root):
            yield i

    def __contains__(self, key):
        node = self.root
        for char in key:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        if node.value:
            return True

    def __str__(self):
        def preorder(node, path=''):
            ret = "%s%s\n" % (' ' * len(path) if len(path) > 1 else '-', path[-1:])
            for char in sorted(node.children):
                curpath = '%s%s' % (path, char)
                ret += preorder(node.children[char], curpath)
                if node.children[char].value:
                    ret += "%s%s\n" % ('-' * len(path), curpath)
            return ret

        return preorder(self.root)

    def _path_exists(self, key):
        node = self.root

        for char in key:
            if char in node.children:
                node = node.children[char]
            else:
                return False

        return True

    def iterkeys(self):
        return self.__iter__()
