#from commitTree import CommitNode
from createRepo import MygitRespostory
from myGit import read_object, createblob 
from simulation import stagingFile
#import datetime
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
    
def createCommitSha(data):
    return data
   
def cmd_commit():
    commit_data = "heellll"
    commit_history_element = {
            'commit' : createCommitSha(commit_data),
            'author': 'Fossele <email>',
            'message': commit_data
           # 'Data': datetime.datetime(0, 0 , 0)
        }
    with open('commit.json', 'r') as file:
         commit_history = json.load(file)
         

    with open('commit.json', 'w') as file:
        commit_history.update(commit_history_element)
        json.dump(commit_history, file, indent=4)
        


def cmd_log():
    with open('commit.json', 'r') as file:
         commit_history = json.load(file)
         
    for commit in commit_history:
        print(commit + "||" + commit_history[commit])     
        
def cmd_init(path):
    "The repository is initialised here"
   # sub_dirs = ["refs","refs/heads", "refs/tags", "HEAD" "objects", "logs", "config", "description"]
    repo = MygitRespostory(path) 
    
def cmd_cat(obj,path="."):
    content = read_object(obj, path)
     
def cmd_hash(filename):
    hash = createblob(filename)
    print(hash)
  
cmd_commit()
cmd_log()