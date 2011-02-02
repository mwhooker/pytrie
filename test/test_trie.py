import unittest
from pytrie import Trie

class TestTrie(unittest.TestCase):

    def setUp(self):
        self.corpus = ['black',
                       'blue',
                       'red',
                       'green',
                       'aqua marine']
        self.fixture = Trie()
        for i in self.corpus:
            self.fixture[i] = True

    def test_len(self):
        assert len(self.fixture) == len(self.corpus)

    def test_storage(self):
        for i in self.corpus:
            assert i in self.fixture

        assert "not a color" not in self.fixture

    def test_delete(self):
        assert self.corpus[0] in self.fixture
        del self.fixture[self.corpus[0]]
        assert self.corpus[0] not in self.fixture

    def test_getitem(self):
        for i in self.corpus:
            assert self.fixture[i] == True
        self.assertRaises(KeyError, self.fixture.__getitem__, 'not a color')
    
    def test_setitem(self):
        self.assertRaises(KeyError, self.fixture.__setitem__, '')

    def test_iterator(self):
        collected_keys = set([k for k in self.fixture])
        assert collected_keys == set(self.corpus)

        for k, v in self.fixture:
            assert v == True

if __name__ == '__main__':
    unittest.main()