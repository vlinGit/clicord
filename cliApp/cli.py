from clicordClass import Clicord
from helper import *

# TODO:
#   Figure out how to make it an actual CLI

def main():
    token, channel = parsecli()
    
    cc = Clicord(token, channel)
    cc.run()
    