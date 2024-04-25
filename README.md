## Creating the Slack App in your workspace

1. Navigate to https://api.slack.com/apps.
2. Click on **"Create New App"** and select **"From Scratch"**.
3. Enter the name for your app and select the workspace you want to install it to.

## Setting Up OAuth and Permissions and obtaining Bot Token

1. In the sidebar on the left, under **"Features"**, click on **"OAuth and Permissions"**.
2. Scroll down to **"Scopes"** and under **"Bot Token Scopes"**, click on **"Add an OAuth Scope"**.
3. Add the following scopes:
   - `app_mentions:read`
   - `chat:write`
   - `chat:write.public`
   - `im:history`
4. Scroll up a bit to **"OAuth Tokens for Your Workspace"** and click on **"Install to Workspace"**.
5. Click on **"Allow"** on the subsequent screen.
6. You will be returned to the **"OAuth and Permissions"** page.
7. Copy the **"Bot User OAuth Token"** and paste it into your `.env` file as the `SLACK_BOT_TOKEN`. It should look something like: `SLACK_BOT_TOKEN="xoxb-aaaaaaaaaaaaaa-bbbbbbbbbbbbb-ccccccccccccccccccccccccc"`.

## Setting Up App-Level Tokens and obtaining App Token

1. In the sidebar on the left, under **"Settings"**, click on **"Basic Information"**.
2. Scroll down to **"App-Level Tokens"**.
3. Click on **"Generate Token and Scopes"**.
4. Name the token anything, for example, **"App Token"**.
5. Click on **"Add Scope"** and add the following scope: `connections:write`.
6. Click on **"Generate"**.
7. Copy the generated token and paste it into your `.env` file as the `SLACK_APP_TOKEN`. It should look something like: `SLACK_APP_TOKEN="xapp-a-bbbbbbbbbbb-ccccccccccccc-ddddddddddddddddddddddddddddddddddddd"`.
8. Click on **"Done"**.

## Enabling Socket Mode

1. In the sidebar on the left, under **"Settings"**, click on **"Socket Mode"**.
2. Make sure **"Enable Socket Mode"** has been toggled **"on"**.

## Enabling Interactivity

1. In the sidebar on the left, under **"Features"**, click on **"Interactivity and Shortcuts"**.
2. Make sure **"Interactivity"** has been toggled **"on"**.

## Setting Up Event Subscriptions

1. In the sidebar on the left, under **"Features"**, click on **"Event Subscriptions"**.
2. Make sure **"Enable Events"** has been toggled **"on"**.
3. Under **"Subscribe to Bot Events"**, click on **"Add Bot User Event"**.
4. Add the following Bot User Events:
   - `app_mention`
   - `message.im`
5. Click on **"Save Changes"** and if prompted, click on **"reinstall app"**.

## Configuring App Home

1. In the sidebar on the left, under **"Features"**, click on **"App Home"**.
2. Under **"Show Tabs"**, make sure **"Messages Tab"** has been toggled **"on"**.
3. Check the box for **"Allow users to send Slash commands and messages from the messages tab"**.

## Adding the App to a channel

1. In the channel you want the bot to reside in, simply mention the bot by typing **"@bot_name"** and press enter.
2. An alternative way is to right click a channel, click on **"Settings"** -> **"Integrations"** -> **"Add Apps"**.
3. You should now be able to interact with the app via **"@bot_name"** mentions.
