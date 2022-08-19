class TrieNode:
    """A node in the trie structure"""
    def __init__(self, char):
        # the character stored in this node
        self.char = char
        # a flag to mark the end of the query and store its frequency.
        self.count = -1
        # a dictionary of child nodes
        # keys are characters, values are nodes
        self.children = {}


class Trie(object):
    def __init__(self):
        """
        Initiate the trie with an empty char
        """
        self.root = TrieNode("")

    def build_tree(self, queries_dict):
        """
        :param queries_dict (dict): format {query string : frequency}
        """
        for query in queries_dict.keys():
            self.insert(query, queries_dict)

    def insert(self, query, queries_dict):
        """Insert a query into the trie"""
        node = self.root
        # Loop through each character in the query string
        # if there is no child containing the character, create a new child for the current node
        for char in query:
            if char in node.children:
                node = node.children[char]
            else:
                # If a character is not found, create a new node in the trie
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        # Mark the end of a query with the frequency counter
        node.count = queries_dict[query]

    def dfs(self, node, prefix):
        """Depth-first traversal of the trie

        :param node (TrieNode): the root of the subtree
        :param prefix (string): the current prefix to form the full queries when traversing the trie
        """
        if node.count != -1:
            self.output.append((prefix + node.char, node.count))

        for child in node.children.values():
            self.dfs(child, prefix + node.char)

    def search(self, x, top_n=10):
        """Given an input (a prefix), find all queries stored in
        the trie starting with the perfix, sort and return top_n queries based on the occurences.
        """
        # Use a variable within the class to keep all possible outputs
        # As there can be more than one word with such prefix
        self.output = []
        node = self.root

        # Check if the prefix is in the trie
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                # cannot found the prefix, return empty list
                return []

        # Traverse the trie to get all candidates
        self.dfs(node, x[:-1])

        # Sort the results in reverse order and return
        self.output.sort(key=lambda x: x[1], reverse=True)

        return self.output[0:top_n]
