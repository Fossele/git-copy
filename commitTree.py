#for simplicity i considered only the committer and not the author of the code

class CommitNode:
    def __init__(self, tree ,committer,parent_commit=[]):
        self.tree = tree
        self.committer = committer
        self.parent_commit = parent_commit
        self.number_of_branches = len(parent_commit)
        
        
    """the parent_commit is pointing to all the possible parents of this commit."""
        
    def print_all_parents(self):
        for parent in self.parent_commit:
            print(parent)
            
    def print_commit(self):
        self.content = "tree "+ self.tree + "\n" + self._parent_commit_to_string()  + "commiter " + self.committer
        print(self.content)
    
    #the helper function below is use to manage the error caused by printing the arrays to list directly into print commit
    def _parent_commit_to_string(self):
         self.parent_commit
         result = ""
         if self.parent_commit:
          for parent in self.parent_commit:
            result += ("parent "+ parent.tree + "\n")
         
         return result   

    
    
        
first = CommitNode("heyyyyyyy","678tee")
second = CommitNode("you","678tee")
third = CommitNode( "678teee","Zen", [first,second]).print_commit()