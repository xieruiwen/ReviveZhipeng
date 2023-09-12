import hashlib
import json
from typing import Dict, Any


from flask import Flask, request


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


app = Flask(__name__)


SIGNING_SECRET = b"xxxx"


def is_valid_signature(signing_secret: bytes, body: bytes, signature: str) -> bool:
    # ref: https://open.seatalk.io/docs/server-apis-event-callback
    return hashlib.sha256(body + signing_secret).hexdigest() == signature




@app.route("/bot-callback", methods=["POST"])
def bot_callback_handler():
    body: bytes = request.get_data()
    signature: str = request.headers.get("signature")
    if not is_valid_signature(SIGNING_SECRET, body, signature):
        return ""
    data: Dict[str, Any] = json.loads(body)
    event_type: str = data.get("event_type", "")
    if event_type == EVENT_VERIFICATION:
        return data.get("event")
    elif event_type == NEW_BOT_SUBSCRIBER:
    # fill with your own code
        pass
    elif event_type == MESSAGE_FROM_BOT_SUBSCRIBER:
    # fill with your own code
        pass
    elif event_type == INTERACTIVE_MESSAGE_CLICK:
    # fill with your own code
        pass
    elif event_type == BOT_ADDED_TO_GROUP_CHAT:
    # fill with your own code
        pass
    elif event_type == BOT_REMOVED_FROM_GROUP_CHAT:
    # fill with your own code
        pass
    elif event_type == NEW_MENTIONED_MESSAGE_RECEIVED_FROM_GROUP_CHAT:
    # fill with your own code
        pass
    else:
        pass
        return ""
    

if __name__ == "__main__":
    app.run(debug=True)