**DISCORD PRICE TICKER BOT**

Set to display price of Algorand and update using Coin Gecko API.

Queries the API every 60 seconds and updates the Discord bot's nickname in channel.

**Edits to the bot script**

To change the display currency, change the 'token_id' in line 21. Formatting can be changed in line 23.

Bot name can be changed in line 34 and nickname prefix in line 27.

Frequency of update can be changed to a different value in seconds in line 19 with respect to rate limiting in Discord docs.

Can be installed on Pi device or hosted online.

**To install and run:**

Create a bot in your Discord developer account and in the OAuth2 section check the 'bot' and 'administrator' boxes.

Copy the link generated and add your bot to the server of choice.

Give the bot 'PRESENCE INTENT' and 'SERVER MEMBERS INTENT' in the 'Bot' section.

Retrieve the secret token from the 'Bot' section in your Discord developer account.

Create a folder and paste the code and insert your Discord bot token in line 45 from your developer account and save.

Open terminal and CD into the folder just created with the command 'cd 'FolderName'.

In terminal, run the command python3 'BotFileName'.py

The bot will now log in and run.

