import argparse
from cmdfns import *

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
commit_parser = subparser.add_parser("commit")
log_parser = subparser.add_parser("log")
branch_parser = subparser.add_parser("branch")
checkout_parser = subparser.add_parser("checkout")

#sub_parsers = parser.add_subparsers(dest="control")

args = parser.parse_args()
cmd = args.command

match cmd:
    case "init":
         cmd_init(args.path)
    case "clone":
        print("great clone")
    case "status":
        print("great status")
    case "push":
        print("great push")   
    case "pull":
        print("great pull")
    case "add":
        print("great add") 
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

#issue to fix: double running