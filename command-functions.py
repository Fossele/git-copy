import os

def cmd_add(*file_name):
                if file_name == ".":
                 #stageAllFiles()
                    return 0;
                else:
                    #stageFileName(file_name)
                    pool = 0                    
                    
def cmd_commit():
    print("create commit")
    
def cmd_init():
    cwd = os.getcwd()
    mgit_dir = f"{cwd}/.mgit"
    os.makedirs(mgit_dir)
    