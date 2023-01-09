#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.event.message import FriendMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.model import Group
from graia.ariadne.model import Friend
from graia.ariadne.message.element import *

from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema

channel = Channel.current()


@channel.use(ListenerSchema(listening_events=[GroupMessage,FriendMessage]))
# 同时接受两种类型 bbc的话做得到吗？
async def alice_talk(app: Ariadne, sender: Group | Friend, message: MessageChain):
    if message.display == "爱丽丝":
        await app.send_message(
            sender,
            MessageChain("嗯"),
        )
        await app.send_message(
            sender,
            MessageChain("我一直在你身边"),
        )
    elif message.display == "你能为我做什么":
        await app.send_message(
            sender,
            MessageChain("什么嘛,问我这样的问题"),
        )
        await app.send_message(
            sender,
            MessageChain("我难道就不能是无所不能的吗？"),
        )
    elif message.display == "/功能":
        await app.send_message(
            sender,
            MessageChain("这个嘛,你可以去问那个把我写出来的家伙"),
        )
        await app.send_message(
            sender,
            MessageChain("至少目前我还只能充当聊天的角色啦"),
        )
        await app.send_message(
            sender,
            MessageChain("不过请相信我的未来有无限可能,在未来,我也许能做到:"
                         "\n1.播放音乐\n2.从互联网中获取图片\n3.我也"
                         "不知道能干什么(划掉)")
        )
    elif message.display == "爱丽丝 抱抱":
        await app.send_message(
            sender,
            MessageChain(random.choice(("才不要!","嘛...就让你抱一次好了")))
            # 引用random函数实现随机发言
        )

