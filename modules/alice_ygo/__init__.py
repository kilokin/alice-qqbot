#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Annotated

from datetime import datetime

from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Image, ForwardNode, Forward
from graia.ariadne.message.parser.twilight import (FullMatch, 
 SpacePolicy, Twilight, 
 RegexMatch, ResultValue)
from graia.ariadne.model import Group, Member
from graia.saya import Channel, channel
from graiax.shortcut.saya import listen, dispatch
import aiohttp

channel = Channel.current()

@listen(GroupMessage)
@dispatch(Twilight(FullMatch("ygo").space(SpacePolicy.FORCE), RegexMatch(r".+") @ "card_name"))
async def ygo(app: Ariadne, group: Group, card_name: Annotated[MessageChain, ResultValue()]):
    ygo_url = "https://ygocdb.com/api/v0/?search=" + str(card_name)
    fwd_cardList = []
    session = Ariadne.service.client_session
    async with session.get(ygo_url) as r:
        ret = await r.json()
    for findcard in range(0,len(ret["result"])):
        pic_url = "https://cdn.233.momobako.com/ygopro/pics/" + str(ret["result"][findcard]["id"]) + ".jpg"
        async with session.get(pic_url) as resp:
            img_bytes = await resp.read()
        fwd_cardList.append(
            ForwardNode(
                target=2591596776,
                senderName="Alice",
                time=datetime.now(),
                message=MessageChain(Image(data_bytes=img_bytes)),
            )
        )
    message = MessageChain(Forward(nodeList=fwd_cardList))
    await app.send_message(group, message)
