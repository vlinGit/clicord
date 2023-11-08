import argparse
import requests
import json

maxHistory = 50

# TODO:
# History is recieved reversed, fix it

# GET requests: https://discord.com/api/v9/channels/<channel id>/messages?limit=<number>
def printHistory(msgCount: int, channel: str, token) -> list[str]:
    header: dict[str, str] = { "Authorization": token,
                               "content-type": "application/json" }
    messages = requests.get(f"https://discord.com/api/v9/channels/{channel}/messages?limit={min(msgCount, 50)}",headers=header)
    
    for message in json.loads(messages.text):
        author: str = message.get("author", {}).get("username", "")
        message: str = message.get("content", "")
        
        if author and message:
            print(f"{author}: {message}")
    
# POST requests: https://discord.com/api/v9/channels/<channel id>/messages
def sendMsg() -> None:
    parser= argparse.ArgumentParser(description="A discord cgi program")
    parser.add_argument("-s", nargs=2, metavar=("token", "channel"), type=str, help="Your auth token and the id of the channel you want to message")
    parser.add_argument("-b", action="store_true", help="Runs the command as a discord bot")
    args: argparse.Namespace = parser.parse_args()
    token, channel = args.s[0], args.s[1]
    
    if args.b:
        token = f"Bot {token}"
    
    request = f"https://discord.com/api/v9/channels/{channel}/messages"
    header: dict[str, str] = { "Authorization": token,
                               "content-type": "application/json"}
    printHistory(10, channel, token)
    
    while True:
        message = input("Message: ")
        payload: dict[str, str] = { "content": message }
        post = requests.post(request,json=payload,headers=header)

if __name__ == "__main__":
    sendMsg()