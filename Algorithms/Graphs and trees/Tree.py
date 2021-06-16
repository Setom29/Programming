class myNode:
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data=data
def bin_search(bin_search_tree, number, path=''):
    if bin_search_tree