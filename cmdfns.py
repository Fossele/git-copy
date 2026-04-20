
from createRepo import MygitRespostory
from myGit import read_object


def cmd_add(*file_name):
   """if the file has """
   
def cmd_commit():
    print("create commit")


def cmd_init(path):
    "The repository is initialised here"
   # sub_dirs = ["refs","refs/heads", "refs/tags", "HEAD" "objects", "logs", "config", "description"]
    repo = MygitRespostory(path)
    
    
def cmt_cat(obj,path="."):
    content = read_object(obj, path)
  
    
