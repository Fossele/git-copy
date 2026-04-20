
from createRepo import MygitRespostory



def cmd_add(*file_name):
    if file_name == ".":
        # stageAllFiles()
        return 0
    else:
        # stageFileName(file_name)
        pool = 0


def cmd_commit():
    print("create commit")
    


def cmd_init(path):
    "The repository is initialised here"
   # sub_dirs = ["refs","refs/heads", "refs/tags", "HEAD" "objects", "logs", "config", "description"]
    repo = MygitRespostory(path)
    
    
    
