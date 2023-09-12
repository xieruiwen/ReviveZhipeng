import httpx
import hashlib
import json
from typing import Dict, Any

from flask import Flask, request

app = Flask(__name__)

BOT_WEBHOOK_URL = "https://openapi.seatalk.io/webhook/group/2GR09OlbSzm0mBqt4GPfOQ"
#BOT_WEBHOOK_URL = "https://openapi.seatalk.io/webhook/group/w-a0CCzIQYyGo7anZqd6HA"


# settings
SIGNING_SECRET = b"82KXQ97A01gCjvYJ84O3p8f0lNovjL9Q"


# event list
# ref: https://open.seatalk.io/docs/list-of-events
EVENT_VERIFICATION = "event_verification"
NEW_BOT_SUBSCRIBER = "new_bot_subscriber"
MESSAGE_FROM_BOT_SUBSCRIBER = "message_from_bot_subscriber"
INTERACTIVE_MESSAGE_CLICK = "interactive_message_click"
BOT_ADDED_TO_GROUP_CHAT = "bot_added_to_group_chat"
BOT_REMOVED_FROM_GROUP_CHAT = "bot_removed_from_group_chat"
NEW_MENTIONED_MESSAGE_RECEIVED_FROM_GROUP_CHAT = "new_mentioned_message_received_from_group_chat"



@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/send-webhook', methods=['POST','GET'])
def send_webhook():
    json_payload = {
        "tag": "text",
        "text": {
            "content": u"咖",
            "at_all": False
        }
    }
    httpx.post(url=BOT_WEBHOOK_URL, json=json_payload)


def is_valid_signature(signing_secret: bytes, body: bytes, signature: str) -> bool:
    # ref: https://open.seatalk.io/docs/server-apis-event-callback
    return hashlib.sha256(body + signing_secret).hexdigest() == signature


@app.route("/bot-callback", methods=["POST",'GET'])
def bot_callback_handler():  
    json_payload = {
                "tag": "text",
                "text": {
                    "content": u"兄弟们我屌不",
                    "at_all": False
                }
            }
    #httpx.post(url=BOT_WEBHOOK_URL, json=body)
    body: bytes = request.get_data()
    signature: str = request.headers.get("signature")
    if not is_valid_signature(SIGNING_SECRET, body, signature):
        return ""
    data: Dict[str, Any] = json.loads(body)
    event_type: str = data.get("event_type", "")
    if event_type == EVENT_VERIFICATION:
        return data.get("event")
    elif event_type == NEW_MENTIONED_MESSAGE_RECEIVED_FROM_GROUP_CHAT:
        httpx.post(url=BOT_WEBHOOK_URL, json=body)
        pass
    else:
        pass
        return ""
    





if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
