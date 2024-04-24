# slack_image_generator
A bot that uses image generation models to respond to a mention in Slack with an AI generated image.

Navigate to https://api.slack.com/apps  
Click on "Create New App" and select "from scratch"  
Name your app and select your workspace  

In the sidebar on the left, under "Features", click on "OAuth and Permissions"  
Scroll down to "Scopes" and under "Bot Token Scopes" click on "Add an OAuth Scope"  
<img src="https://github.com/ndkma/slack_image_generator/assets/102197063/214985f7-86b3-4594-9a9a-2dedf08d0e18" width="700" height="300">

Add the following scopes:  
-app_mentions:read  
-chat:write  
-chat:write.public  
-im:history  
