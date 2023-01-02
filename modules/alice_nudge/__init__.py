#!/usr/bin/env python
# -*- coding: utf-8 -*-

from graia.ariadne.app import Ariadne
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.model import Group
from graia.ariadne.model import Friend
from graia.ariadne.event.mirai import NudgeEvent

from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema

import random

channel = Channel.current()

@channel.use(ListenerSchema(listening_events=[NudgeEvent]))
async def getup(app: Ariadne, event: NudgeEvent):
    match event.context_type:
        case "group":
            await app.send_group_message(
                event.group_id,
                MessageChain(random.choice(
                    ("不要戳我啦，好痒",
                    "啊？再这样我要生气了哦")))
            )
        case "friend":
            await app.send_friend_message(
                event.friend_id,
                MessageChain("嗯，请问有什么事吗？")
            )
        case _:
            return
