##Discord Bot

This Discord bot is connected with ChatGPT to answer all of your questions. 
It is coded in Python and optimized for programming questions, but can work with any question you have.

Follow these steps to set up your own bot:

1) Install the Discord library: pip install discord

2) Get an API key from ChatGPT:
    Log in or sign up for ChatGPT at https://chat.openai.com/.
    Go to the following page with your account: https://platform.openai.com/account/api-key
    
    And then create a new secret key and save it
    
3) Create a Discord bot and get its API key:
    Go to https://discord.com/developers/applications with your Discord account.
    Click on "New Application" and choose a bot name. Accept the policies.
    Go to "Bot" and click on "Add Bot". Click on "Show Token" and save it.
    Go to "OAuth" and select the following options:
    
  In "Scopes": 
   - Bot
  
  In "Bot Permissions":
   - Read Messages/View Channels
   - Manage Messages
   - Read Message History
   - Embed Links
   - Use Slash Commands
   
   And finally invite your bot to a server
    
4) Download the files and open them in your favorite IDE. Replace the following keys:
    In "API_KEY", put your ChatGPT key.
    In "TOKEN", put your Discord key.

This bot has two commands:

    $ping: Test that the bot has permissions to send messages in the channel.
    $gpt: Ask a question to ChatGPT.

 
    
