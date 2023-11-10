import argparse

def parsecli() -> (str, str):
    parser= argparse.ArgumentParser(description="A discord cgi program")
    parser.add_argument("-s", nargs=2, metavar=("token", "channel"), type=str, help="Your auth token and the id of the channel you want to message")
    parser.add_argument("-b", action="store_true", help="Runs the command as a discord bot")
    args: argparse.Namespace = parser.parse_args()
    token, channel = args.s[0], args.s[1]
    if args.b:
        token = f"Bot {token}"
    
    return token, channel
