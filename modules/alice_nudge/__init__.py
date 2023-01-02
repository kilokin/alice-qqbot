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
            a = random.randint(1,2)
            # 令爱丽丝随机发言，我知道这样实现很蠢
            # 但水平低，想不出别的办法力（悲）
            if a == 1:
                await app.send_group_message(
                    event.group_id,
                    MessageChain("不要戳我啊,好痒")
                    )
            else:
                await app.send_group_message(
                    event.group_id,
                    MessageChain("啊?再这样我要生气了哦")
                    )
        case "friend":
            await app.send_friend_message(
                event.friend_id,
                MessageChain("嗯，请问有什么事吗？")
            )
        case _:
            return
