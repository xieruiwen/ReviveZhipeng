# -*- coding: UTF-8 -*-
import httpx
import base64
import sys
import os
import random

BOT_WEBHOOK_URL = "https://openapi.seatalk.io/webhook/group/2GR09OlbSzm0mBqt4GPfOQ"

json_payload = {
    "tag": "text",
    "text": {
        "content": u"没事，我在你身边",
        "at_all": False
     }
}
httpx.post(url=BOT_WEBHOOK_URL, json=json_payload)
