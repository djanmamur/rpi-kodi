from typing import Dict, Coroutine

import aiohttp


def async_post(url: str = "", body: Dict = None, headers: Dict = None) -> Coroutine:
    if body is None:
        body = {}
    if headers is None:
        headers = {}

    async with aiohttp.ClientSession as session:
        async with session.post(url=url, data=body, headers=headers) as result:
            result.raise_for_status()
            return result.json()


def async_get(url: str = "") -> Coroutine:
    async with aiohttp.ClientSession as session:
        async with session.get(url=url) as result:
            result.raise_for_status()
            return result.json()
