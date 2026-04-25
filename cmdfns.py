from commitTree import CommitNode
from createRepo import MygitRespostory
from myGit import read_object, createblob 
from simulation import stagingFile
import json


def cmd_add(file_names):
    data = {}
    for file_name in file_names:  
        data.update(stagingFile(file_name))
   
   
    with open("data.json", "r") as file:
        stagingArea = json.load(file)
    
    with open('data.json', 'w') as file:
           stagingArea.update(data)
           json.dump(stagingArea, file, indent=4)
           #print(stagingArea)
    
   
   
def cmd_commit():
    print("create commit")


def cmd_init(path):
    "The repository is initialised here"
   # sub_dirs = ["refs","refs/heads", "refs/tags", "HEAD" "objects", "logs", "config", "description"]
    repo = MygitRespostory(path)
    
    
def cmd_cat(obj,path="."):
    content = read_object(obj, path)
    
    
def cmd_hash(filename):
    hash = createblob(filename)
    print(hash)
  
commit1 = CommitNode("abc123", "maximus", "hey")
commit2 = CommitNode("abc1267", "maximus", "cute",commit1)
commit3 = CommitNode("abc12389", "maximus", "good",commit2)
    
def cmd_log(latest_commit):
    print(latest_commit.tree)
    print(latest_commit.committer)
   
    if(latest_commit.parent_commit):
         print(latest_commit.parent_commit)
         cmd_log(latest_commit.parent_commit)
  
  
