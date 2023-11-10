# clicord
WIP discord cli program

# DISCLAIMER
I am not responsible for anything that may occur with the use of this program. If you get banned for violating TOS or have info leaked that is entirely on you.

### About
clicord is a small project I'm working on that allows for a cli interface for discord text communication. Not really sure how advance I want this to be but the general features I want is to be able to send/delete/view messages from a specified channel in discord. 

### How to use
Click on a release version and follow the instructions to install
 
You'll need your auth token which can be found by doing the following:

**IMPORTANT**: DO NOT SHARE YOUR AUTH TOKEN!!!
<ol>
<li>Open and login to discord on a browser</li>
<li>Open the network tab in the developer console of your browser, if you see nothing refresh the page</li>
<li>Find a request for the file "country-code" and open it</li>
<li>In the headers, find "Authorization" and everything to the right of it is your auth token</li>
</ol>

For the channel id:
<ol>
<li>Enable discord developer mode</li>
<li>Right click the channel you want to message</li>
<li>Click "Copy Channel Id"</li>
</ol>

Now for the actual command:

<code>python clicord.py -s \<auth token\> \<channel id\></code>

Replace the parts with brackets with the information you have obtained and click enter. You'll be shown a brief history of the messages in the channel and be prompted to enter a message. Type whatever you want and click enter and your message will show up in the channel. 

### Messaging with a bot
Add a `b` flag to the command and use the bot's auth token:

<code>python clicord.py -b -s \<bot auth token\> \<channel id\></code>

### Terminating the program
If you want to terminate the program press CTRL+C.

### TODO
<ul>
<li>Delete message</li>
<li>OAuth (You currently must know your auth token)</li>
</ul>
