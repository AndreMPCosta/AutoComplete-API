import unittest
from csv import reader
from typing import List


def get_words(file: str) -> List[str]:
    """Retrieve all the words in the csv file"""
    words = []
    with open(file) as csv_file:
        list_words = reader(csv_file)
        for word in list_words:
            words += word
    return words


class Node:
    """
    A class used to represent a Node

    ...

    Attributes
    ----------
    data : str
    children: dict
        contains all the children nodes
    """
    def __init__(self, data):
        self.data = data
        self.children = {}

    def __repr__(self):
        return str(self.data) + str(self.children)


class Trie:
    """
        A class used to represent a Trie (https://en.wikipedia.org/wiki/Trie)

        ...

        Attributes
        ----------
        root : node
            The root node, in this case, we will use 'Start' string
        end: node
            The final node for a word, it will be called 'End'
        """
    def __init__(self, words):
        """
        Parameters
        ----------
        words: List
            The words to be inserted on the Trie, each char is a node
        """
        self.root = Node('Start')
        self.end = Node('End')
        # Building our trie using the add_word method
        for word in words:
            # Since in ASCII, for example, 'a' is different than 'A', and it would lead
            # to different keys in the dictionary, every char in the word is converted to lowercase to avoid this
            self.add_word(word.lower())

    def __repr__(self):
        return str(self.root)

    def add_word(self, word: str):
        """Adds a new word to our Trie

        Parameters
        ----------
        word : The word that should be inserted
        """

        # Start inserting in the beginning of the Trie, on the root node
        next_node = self.root
        for char in word:
            if char in next_node.children:
                # If the char is already a node, it navigates to that specific node
                next_node = next_node.children[char]
            else:
                # In this case, the char is not present in the children, so it is needed to create a new node and point
                # to it
                new_node = Node(char)
                next_node.children[char] = new_node
                next_node = new_node
        # Finishing insertion by inserting the end node
        next_node.children['End'] = self.end

    def _build_words(self, node: Node, prefix: str) -> List[str]:
        """Navigates through the Trie to get all the possible outcomes from a specific prefix

        Parameters
        ----------
        node : The node to start iterating
        prefix: The prefix to be used
        """
        output = []
        # Iterate through each child to cover all the possibilities
        for child in node.children:
            if child == 'End':
                # In the end, the "prefix" argument is already the full word, because of the recursion being
                # employed here, see next line, so we add it to the output list
                output.append(prefix)
            else:
                # New node to start, plus changing to the next prefix (+1 char)
                output.extend(self._build_words(node.children[child], prefix+child))

        return output

    def get_words(self, prefix):
        """Find the starting node (after the last letter of the prefix)

        Parameters
        ----------
        prefix: The prefix to be used on this search
        """
        # Start on the root node
        next_node = self.root
        # Iterate until we find the starting node
        for char in prefix:
            if char in next_node.children:
                next_node = next_node.children[char]
            else:
                return []
        # Use the starting node, plus the prefix on the _build_words method
        return self._build_words(next_node, prefix)


class TestMethods(unittest.TestCase):

    def test_190titles_csv(self):
        trie = Trie(get_words('test_files/190titles.csv'))
        self.assertEqual(trie.get_words('fac'), ['facebook', 'facebook lite', 'facebook pages manager'])

    def test_manual_input(self):
        trie = Trie(['hi', 'hello', 'howdy', 'help', 'hell', 'hello be'])
        self.assertEqual(trie.get_words('he'), ['hello', 'hello be', 'hell', 'help'])

    def test_6500titles_csv(self):
        trie = Trie(get_words('test_files/6500titles.csv'))
        self.assertEqual(trie.get_words('ub'), ['uber driver', 'ubersync'])


# Loading for the flask app
trie = Trie(get_words('test_files/6500titles.csv'))

if __name__ == '__main__':
    unittest.main()

