import argparse
from cmdfns import *

"""the following are the parsers used to take commands from the user"""

parser = argparse.ArgumentParser( prog="mygit")
parser.add_argument("mygit")

subparser = parser.add_subparsers(dest = "command")

init_parser = subparser.add_parser("init", help="Innitialise a new,empty repository.")
init_parser.add_argument("path", nargs="?",default=".", help="Enter a path to initialise.")
#init_parser.add_argument("")

status_parser = subparser.add_parser("status")
push_parser = subparser.add_parser("push")
pull_parser = subparser.add_parser("pull")

add_parser = subparser.add_parser("add")
add_parser.add_argument("-a", "--all", help="Stages all changes in the entire repository,egardless of your current directory.")
add_parser.add_argument("filename", nargs="+", help="stages all given files.")

hash_parser= subparser.add_parser("hash-object")
hash_parser.add_argument("-w", dest="write", help="write the object into the object database.")
hash_parser.add_argument("-t", metavar="type", dest="type", choices=["blob", "tree", "commit", "tag"], default="blob", help="specify the type.")
hash_parser.add_argument("filename", help="Enter the file to hash")


cat_parser= subparser.add_parser("cat-file")
cat_parser.add_argument("-t", metavar="type", dest="type", choices=["blob", "tree", "commit", "tag"], default="blob", help="specify the type.")
cat_parser.add_argument("-w", dest="write", help="write the object into the object database.")
cat_parser.add_argument("object", help="object to read")



commit_parser = subparser.add_parser("commit")
log_parser = subparser.add_parser("log")
branch_parser = subparser.add_parser("branch")
checkout_parser = subparser.add_parser("checkout")

#sub_parsers = parser.add_subparsers(dest="control")

args = parser.parse_args()
cmd = args.command

"""our commands are run from here using this match cases. Also i may turn this file to the main file"""
match cmd:
    case "init":
         cmd_init(args.path)
    case "cat-file":   
          cmt_cat(args.object)    
       
    
    case "clone":
        print("great clone")
    case "status":
        print("great status")
    case "push":
        print("great push")   
    case "pull":
        print("great pull")
    case "add":
        pass
    case "commit":
        print("great commit")  
    case "branch":
        print("great branch")   
    case "checkout":
        print("great checkout")  
    case "log":
        print("great log")
    case _:
        print("Too bad, unknown case")

