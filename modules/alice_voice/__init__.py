#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from graia.ariadne.app import Ariadne
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Voice
from graia.saya import Channel
from graiax import silkcoder
# silkcoder用于将音频转换为silk
from graia.scheduler.saya import SchedulerSchema
from graia.scheduler import timers

channel = Channel.current()
group_id = 765567564 #这里是你想要发送消息的QQ群

@channel.use(SchedulerSchema(timers.crontabify("30 22 * * * 30")))
# 设定22时30分30秒定时任务
async def goodnight(app: Ariadne):
    voice_bytes_night = await silkcoder.async_encode(Path("data", "voice", "goodnight.m4a",ios_adaptive = True))
    # 使用silkcoder将音频转换为silk形式
    # 因为iOS 客户端的只能播放 25kbps 以下（不含） 码率的音频
    # 需设定ios_adaptive参数为True
    await app.send_group_message(
        group_id, 
        MessageChain("已经是晚上十点半了哦，晚安")
    )
    await app.send_group_message(
        group_id, 
        MessageChain(Voice(data_bytes=voice_bytes_night))
    )

@channel.use(SchedulerSchema(timers.crontabify("35 7 * * * 30")))
# 设定7时30分30秒执行任务
async def goidmorning(app: Ariadne):
    voice_bytes_morning = await silkcoder.async_encode(Path("data", "voice", "goodmorning.m4a",ios_adaptive = True))
    await app.send_group_message(
        group_id, 
        MessageChain("现在是早上七点35分，早安")
    )
    await app.send_group_message(
        group_id, 
        MessageChain(Voice(data_bytes=voice_bytes_morning))
    )
