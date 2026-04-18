import os


def cmd_add(*file_name):
    if file_name == ".":
        # stageAllFiles()
        return 0
    else:
        # stageFileName(file_name)
        pool = 0


def cmd_commit():
    print("create commit")


def cmd_init():
    sud_dir = ["refs", "objects", "logs"]
    cwd = os.getcwd()
    mgit_dir = os.path.join(cwd, ".mgit")
    if not os.path.exists(mgit_dir):
       os.makedirs(mgit_dir)
    print(mgit_dir)
    for sub in sud_dir:
        sub_path = os.path.join(mgit_dir, sub)
        if not os.path.exists(sub_path):
           os.makedirs(sub_path)
        print(sub_path)


cmd_init()