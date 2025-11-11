import asyncio
import os

import botpy
from botpy import logging
from botpy.ext.cog_yaml import read
from botpy.message import C2CMessage
from ollama import Client

olm_client = Client(host="127.0.0.1:11434")

log = logging.get_logger()


def chat(message):
    messages = [{
        "role": "system",
        "content": """
        你是一个机器人，用中文回复用户问题
        """
    },
        {
            "role": "user",
            "content": message.content
        }
    ]
    response = olm_client.chat(
        model="llama3:latest",
        messages=messages,
    )
    print(response)
    return response["message"]["content"]


class MyClient(botpy.Client):
    async def on_ready(self):
        log.info(f"robot onread")

    async def on_c2c_message_create(self, message: C2CMessage):
        content = chat(message=message)
        print(content)
        message_result = await message._api.post_c2c_message(
            openid=message.author.user_openid,
            msg_type=0, msg_id=message.id,
            content=content
        )
        log.info(message_result)


if __name__ == "__main__":
    intents = botpy.Intents(public_messages=True)
    client = MyClient(intents=intents, is_sandbox=True)
    client.run(appid="102464888", secret="jR9raJ2lUDwgQAueO8tePAvgSE0mYK6t")
