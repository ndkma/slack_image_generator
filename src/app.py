import requests
import os, logging
import slack_bolt
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack import WebClient
from dotenv import load_dotenv
import io
from PIL import Image

# Credentials
load_dotenv()
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]
headers = {"Authorization": f"Bearer {os.getenv('AUTH_TOKEN')}"}

app = App(token=SLACK_BOT_TOKEN)
client = WebClient(SLACK_BOT_TOKEN)
logger = logging.getLogger(__name__)

API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"

# ====================================
# Event listener
# ====================================

@app.event(("app_mention"))
def handle_app_mention_event(body: dict, say: slack_bolt.Say, logger: logging.Logger) -> None:
    user_id = body['event']['user']
    output_channel = body['event']['channel']
    user_message = body['event']['text'].split('>')[1].strip()
    print(user_message)

    # From HF documentation
    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.content

    image_bytes = query({
        "inputs": user_message
    })
    
    image = Image.open(io.BytesIO(image_bytes))
    image.save("image.png")
    file_path = "image.png"  # Replace with the path to your file

    # Upload the file
    result = app.client.files_upload(
        channels=output_channel,
        initial_comment=f"<@{user_id}> asked for an image of: {user_message}!",
        file=file_path
    )

    # Check if the file upload was successful
    if result["ok"]:
        say(f"File uploaded successfully!")
    else:
        say(f"Error uploading file: {result['error']}")

# ====================================
# Initialisation
# ====================================

if __name__ == "__main__":
    # Create an app-level token with connections:write scope
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()
