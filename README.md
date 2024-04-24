# slack_image_generator
A bot that uses image generation models to respond to a mention in Slack with an AI generated image.

Navigate to https://api.slack.com/apps  
Click on "Create New App" and select "from scratch"  
Name your app and select your workspace  

In the sidebar on the left, under "Features", click on "OAuth and Permissions"  
Scroll down to "Scopes" and under "Bot Token Scopes" click on "Add an OAuth Scope"  

Add the following scopes:  
-app_mentions:read  
-chat:write  
-chat:write.public  
-im:history  

Scroll up a bit to "OAuth Tokens for Your Workspace" and click on "Install to Workspace"  
Now, there should be a "Bot User OAuth Token" that you can copy and paste into your .env file as the SLACK_BOT_TOKEN  
It should look something like: SLACK_BOT_TOKEN="xoxb-aaaaaaaaaaaaaa-bbbbbbbbbbbbb-ccccccccccccccccccccccccc"

In the sidebar on the left, under "Settings", click on "Basic Information"  
Scroll down a bit to "App-Level Tokens"  
Click on "Generate Token and Scopes"  
Name the token anything, for example "App Token"  
Click on "Add Scope"  

Add the following scopes:  
-connections:write  
Click on "Generate"  
Now there should be a token that you can copy and paste into your .env file as the SLACK_APP_TOKEN  
It should look something like SLACK_APP_TOKEN="xapp-a-bbbbbbbbbbb-ccccccccccccc-ddddddddddddddddddddddddddddddddddddd"  
Click on "Done"  

In the sidebar on the left, under "Settings", click on "Socket Mode"  
Make sure Enable Socket Mode has been toggled on  

In the sidebar on the left, under "Features", click on "Interactivity and Shortcuts"  
Make sure Interactivity has been toggled on  

In the sidebar on the left, under "Features", click on "Event Subscriptions"  
