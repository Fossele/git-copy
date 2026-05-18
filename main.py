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

checkout_parser = subparser.add_parser("checkout", help="checkout a commit")
checkout_parser.add_argument("commit", help="commit to checkout")
checkout_parser.add_argument("directory to checkout", help="commit to checkout")

#sub_parsers = parser.add_subparsers(dest="control")

args = parser.parse_args()
cmd = args.command

"Here the main commands are executed using match-case"

if __name__ == "__main__":
 match cmd:
    case "init":
         cmd_init(args.path)
    case "cat-file":   
          cmd_cat(args.object)    
    case "hash-object":
          cmd_hash(args.filename)
    case "add":
         cmd_add(args.filename)
    case "log":
         cmd_log()      
    case "checkout":
         cmd_checkout()       
    case "clone":
         cmd_clone()   
    case "status":
        cmd_status()   
    case "push":
        cmd_push(options)    
    case "pull":
        cmd_pull(directory)
    case "commit":
        cmd_commit()  
    case "branch":
        cmd_branch()
           
    case _:
        print("Too bad, unknown case")

