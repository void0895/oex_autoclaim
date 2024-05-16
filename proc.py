import requests


# url
auth_url = "https://api.agiex.org/auth/connect"
info_url = "https://oex-hub-app-api-dot-elite-crossbar-345112.uc.r.appspot.com/mission/get/mission"
reward_url = "https://api.agiex.org/avatar/getReward"



def auth(data):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json;charset=UTF-8",
        "User-Agent": "okhttp/4.9.2"
    }
    r =  requests.post(auth_url, data=data, headers=headers)
    return r.json().get('token')

def info(data):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json;charset=UTF-8",
        "User-Agent": "okhttp/4.9.2"
    }
    r =  requests.post(info_url, data=data, headers=headers)
    return r.json().get('doc', {})

def reward(token):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": "okhttp/4.9.2",
        "Authorization": f"Bearer {token}",
        "Accept-Encoding": "gzip"
    }
    data = '{"aid":1480}'
    r =  requests.post(reward_url, data=data, headers=headers)
    if r.json().get('error'):
        print("skipping")
    else:
        print("success")



