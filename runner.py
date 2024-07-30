import asyncio
import aiohttp
from time import sleep
from os import system
from tenacity import retry, wait_fixed, stop_after_attempt
# url
auth_url = "https://api.agiex.org/auth/connect"
reward_url = "https://api.agiex.org/avatar/getReward"
reward_data = '{"aid":1480}'


@retry(wait=wait_fixed(2), stop=stop_after_attempt(5))
async def auth(session, data, identity):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json;charset=UTF-8",
        "User-Agent": "okhttp/4.9.2"
    }
    async with session.post(auth_url, data=data, headers=headers) as response:
        if response.status == 200:
            json_data = await response.json()
            token = json_data.get('token')
            address = json_data['user']['address']
            reward_data = await reward(token, identity)
            result_save(f"identity = {identity} output = {
                        reward_data}  address =  {address}")
        else:
            raise


@retry(wait=wait_fixed(2), stop=stop_after_attempt(5))
async def reward(token, identity):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": "okhttp/4.9.2",
        "Authorization": f"Bearer {token}",
        "Accept-Encoding": "gzip"
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(reward_url, data=reward_data, headers=headers) as response:
            if response.status == 200:
                json_data = await response.json()
                if json_data.get('error'):
                    print(f"skipping {identity}")
                    return "skipping"
                else:
                    print("success")
                    return "success"
            else:
                raise


def buffer(filename):
    with open(filename, "r") as f:
        temp = f.readlines()
        return [x.strip() for x in temp]


def result_save(data):
    with open("res.txt", "a") as f:
        f.write(str(data))
        f.write("\n")


async def main():
    id_list = buffer("tokens.txt")
    batch_size = int(len(id_list) / 5)
    remainder = int(len(id_list) % 5)
    async with aiohttp.ClientSession() as session:
        for x in range(0, len(id_list), batch_size):
            tasks = [auth(session, id_list[i], identity=i)
                     for i in range(x, batch_size+x)]
            await asyncio.gather(*tasks)
            await asyncio.sleep(10)


while 1:
    system("rm -rf res.txt")
    asyncio.run(main())
    sleep(291480)
