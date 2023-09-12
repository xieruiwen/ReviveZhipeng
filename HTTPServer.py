from flask import Flask, jsonify
import httpx
import hashlib
import json
from typing import Dict, Any

app = Flask(__name__)

#BOT_WEBHOOK_URL = "https://openapi.seatalk.io/webhook/group/2GR09OlbSzm0mBqt4GPfOQ"
BOT_WEBHOOK_URL = "https://openapi.seatalk.io/webhook/group/w-a0CCzIQYyGo7anZqd6HA"

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
    response = httpx.post(url=BOT_WEBHOOK_URL, json=json_payload)

    if response.status_code == 200:
        return jsonify({"message": "Webhook sent successfully!"}), 200
    else:
        return jsonify({"message": "Failed to send webhook."}), 400


if __name__ == "__main__":
    app.run(debug=True)
