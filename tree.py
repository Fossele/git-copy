class Tree:
    "contains data like directories and can be traversed"
    def __init__(self, data):
        self.parent = None
        self.children = []
        self.data = data
        
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def traverse(self):
        if(self.children):
           for sub_node in self.children:
                  print(sub_node.data)
                  if sub_node.children:
                      sub_node.traverse()
                      
class MerkleTree:
    def __init__(self, root):
        self.leaves = []
        self.root = root
        
        
        
        
        
    
       