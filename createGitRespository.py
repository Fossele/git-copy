import os

class MgitRespostory(object):
    workdir = None
    git_obj_path = None
    
    #take in the current work directory 
    def __init__(self, workdir):
        self.workdir = workdir
        self.git_obj_path = None
        self.git_refs_path = None
        self.git_index_path = None
        self.git_head_path = None
        self.git_config_path = None
        
        
     #creates a .mgit object with the workdirectory path 
    def createGitObjectFolder(self): 
        self.gitDir = self._create_path(self.workdir, "/.mgit")
        self._createMetadata(self.gitDir)
    
    def _createMetadata(self, git_path):
        self.git_obj_path = self._create_path(git_path, "objects/") 
        self.git_refs_path = self._create_path(git_path, "refs/")
        self.git_index_path = self._create_path(git_path, "index")
        self.git_head_path = self._create_path(git_path, "HEAD")
        self.git_config_path = self._create_path(git_path, "config")
        
       
    def _create_path(self, git_path, *path):
        return os.path.join(git_path, *path) 
     
    