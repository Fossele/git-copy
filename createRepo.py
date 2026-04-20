import os
#import configparser (though for later use, it will be needed for git configurations such as name, emails, authentication etc)

class MygitRespostory(object):
    """The repository class with fuction for path manage and class creation"""
    workdir = None
    git_obj_path = None
    
    #take in the current work directory 
    def __init__(self, workdir = "."):
        self.workdir = workdir
        self.git_obj_path = None
        self.git_refs_path = None
        self.git_index_path = None
        self.git_head_path = None
        self.git_config_path = None
        self.git_description_path = None
        self.git_all_path = [self.git_obj_path,self.git_refs_path, self.git_description_path,self.git_index_path,self.git_head_path,self.git_config_path]
        self.createGitFolder()
        
        
     #creates a .mgit object with the workdirectory path 
    def createGitFolder(self): 
        self.gitDir = self._create_path(self.workdir, ".mgit")
        self._createMetadata(self.gitDir)
        self.git_all_path = [self.git_obj_path,self.git_refs_path ,self.git_description_path,self.git_index_path,self.git_head_path,self.git_config_path]
        self._create_repo_dir()
    
    def _createMetadata(self, git_path):
        self.git_obj_path = self._create_path(git_path, "objects")    
        self.git_refs_path = self._create_path(git_path, "refs")
        self.git_index_path = self._create_path(git_path, "index")
        self.git_head_path = self._create_path(git_path, "HEAD")
        self.git_config_path = self._create_path(git_path, "config")
        self.git_description_path = self._create_path(git_path, "description")
        
       
    def _create_path(self, git_path, *path):
        
        return os.path.join(git_path, *path) 
    
    def _create_repo_dir(self):
        for path in self.git_all_path:
    
          if  os.path.exists(path):
              print(path)
          else:
             
             if path == self.git_head_path:
                 with open(path, "w") as f:
                     f.write("ref: refs/heads/master\n")
             if path == self.git_description_path:
                 with open(path, "w") as f:
                        f.write("Will contain all your descriptions")
             else:
                 os.makedirs(path)          
        print(f"New repository created at {self.workdir}")
        
        


     
    