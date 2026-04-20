import argparse
"""
    parser = argparse.ArgumentParser()
parser.add_argument("message")

args = parser.parse_args()

print(args.message)
    """
    
parser = argparse.ArgumentParser()
#parser.add_argument("bar")
#parser.parse_args(["BAR"])
parser.add_argument('--foo')
parser.parse_args(['--foo', 'FOO'])

#
#parser.parse_args(['--foo', 'FOO'])
#parser.print_help()
