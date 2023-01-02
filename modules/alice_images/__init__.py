#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

from pathlib import Path

from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.model import Group

from graia.saya import Channel
from graia.ariadne.message.element import Image
from graia.saya.builtins.broadcast.schema import ListenerSchema

channel = Channel.current()

@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def img(app: Ariadne, group: Group, message: MessageChain):
    if message.display == "爱丽丝 贴贴":
        a = random.randint(1,2)
        if a == 1:
            await app.send_message(
                group, 
                MessageChain(Image(path=Path("data", "imgs", "yes.png")))
            )
        else:
            await app.send_message(
                group, 
                MessageChain(Image(path=Path("data", "imgs", "no.png")))
            )
