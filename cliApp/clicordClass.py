import requests
import json
import threading
import time
import sys

# GET requests: https://discord.com/api/v9/channels/<channel id>/messages?limit=<number>
# POST requests: https://discord.com/api/v9/channels/<channel id>/messages
flag = True

class Clicord:
    def __init__(self, token, channel) -> None:
        self.maxHistory = 50
        self.token = token
        self.channel = channel
        self.request = f"https://discord.com/api/v9/channels/{self.channel}/messages"
        self.header: dict[str, str] = { "Authorization": self.token, "content-type": "application/json"}
        
        self.printThread = threading.Thread(target=self.checkHistory)
        self.msgThread = threading.Thread(target=self.postMessages)

    def getMessages(self, msgCount: int) -> list[str]:
        global history
        header: dict[str, str] = { "Authorization": self.token, "content-type": "application/json" }
        messages = requests.get(f"https://discord.com/api/v9/channels/{self.channel}/messages?limit={min(msgCount, self.maxHistory)}",headers=header)

        holder: list[str] = []
        try:
            for message in json.loads(messages.text):
                author: str = message.get("author", {}).get("username", "")
                comment: str = message.get("content", "")
                timestamp: str = message.get("timestamp", "")
                
                if author and message:
                    holder.append(f"{timestamp} {author}: {comment}")
                    
            return holder
        except:
            print("An error occurred during message retrieval")
    
    def printHistory(self, history: list[str]) -> None:
        history.sort()
        for msg in history:
            print(msg)

    def filterNewMessages(self, history: list[str], pre: list[str]) -> None:
        toPrint = []
        
        for i in range(len(history)):
            if history[i] not in pre:
                toPrint.append(history[i])
                
        return toPrint
    
    def checkHistory(self) -> None:
        global flag
        history = self.getMessages(10)
        pre = history

        self.printHistory(history)
        try:
            while flag:
                history = self.getMessages(10)
                toPrint = self.filterNewMessages(history, pre)
                if toPrint:
                    self.printHistory(toPrint)
                    pre.extend(toPrint)
                if len(pre) > 20:
                    pre = pre[10:]
                time.sleep(1)
        except KeyboardInterrupt:
            flag = False
            sys.exit(0)

    def postMessages(self) -> None:
        global flag
        try:
            while flag:
                message = input()
                sys.stdout.write("\033[A\033[2K")
                payload: dict[str, str] = { "content": message }
                requests.post(self.request,json=payload,headers=self.header)
        except (KeyboardInterrupt, EOFError):
            print("Terminating Program")
            flag = False
            sys.exit(0)
    
    def run(self):
        self.printThread.start()
        self.msgThread.start()
        