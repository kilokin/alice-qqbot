#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from graia.ariadne.app import Ariadne
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import *
from graia.saya import Channel
from graiax import silkcoder
from graia.scheduler.saya import SchedulerSchema
from graia.scheduler import timers

channel = Channel.current()
group_id = 765567564

@channel.use(SchedulerSchema(timers.crontabify("30 22 * * * 30")))
# 设定22时30分30秒定时任务
async def goodnight(app: Ariadne):
    voice_bytes_night = await silkcoder.async_encode(Path("data", "voice", "goodnight.m4a"))
    await app.send_group_message(
        group_id, 
        MessageChain("晚安,米娜桑")
    )
    await app.send_group_message(
        group_id, 
        MessageChain(Voice(data_bytes=voice_bytes_night))
    )

@channel.use(SchedulerSchema(timers.crontabify("30 7 * * * 30")))
async def goidmorning(app: Ariadne):
    voice_bytes_morning = await silkcoder.async_encode(Path("data", "voice", "goodmorning.m4a"))
    await app.send_group_message(
        group_id, 
        MessageChain("早安,米娜桑")
    )
    await app.send_group_message(
        group_id, 
        MessageChain(Voice(data_bytes=voice_bytes_morning))
    )
