#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Annotated

import aiohttp
from yarl import URL
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Image
from graia.ariadne.message.parser.twilight import (FullMatch,
                                                   SpacePolicy, Twilight,
                                                   RegexMatch, ResultValue)
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.ariadne.util.saya import listen, dispatch

channel = Channel.current()

@listen(GroupMessage)
@dispatch(Twilight(FullMatch("/番剧查询").space(SpacePolicy.FORCE), RegexMatch(r".+") @ "anime_name"))
async def anime(app: Ariadne, group: Group, anime_name: Annotated[MessageChain, ResultValue()]):
    bangumi_headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/84.0.4147.135 Safari/537.36"}
    url = URL("https://api.bgm.tv/search/subject/") / str(anime_name).strip() % {
        "type": 2,
        "responseGroup": "Large",
        "max_results": 1
    }
    async with aiohttp.request("GET", url, headers = bangumi_headers) as r:
        data = await r.json()

    if "code" in data.keys() and data["code"] == 404:
        await app.send_group_message(group, MessageChain('抱歉啦,爱丽丝没有找到相关信息'))
        return

    detail_url = f'https://api.bgm.tv/subject/{data["list"][0]["id"]}?responseGroup=medium'
    async with aiohttp.ClientSession() as session:
        async with session.get(detail_url) as r:
            data = await r.json()
        async with session.get(data["images"]["large"]) as r:
            img = await r.read()
    await app.send_group_message(group, MessageChain([
        Image(data_bytes=img),
        f"名字:{data['name_cn']}({data['name']})\n"
        f"简介:{data['summary']}\n"
        f"bangumi评分:{data['rating']['score']}(参与评分{data['rating']['total']}人)\n"
        f"bangumi排名:{data['rank']}" if 'rank' in data else ''
        ]))
