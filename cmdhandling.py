import argparse

parser = argparse.ArgumentParser( prog="mgit")
parser.add_argument("mygit")

subparser = parser.add_subparsers(dest = "command")
subparser.add_parser("init")
subparser.add_parser("status")
subparser.add_parser("push")
subparser.add_parser("pull")
subparser.add_parser("add")
subparser.add_parser("commit")
subparser.add_parser("log")
subparser.add_parser("branch")
subparser.add_parser("checkout")

#sub_parsers = parser.add_subparsers(dest="control")

args = parser.parse_args()
cmd = args.command

match cmd:
    case "init":
        print("good dude")
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

