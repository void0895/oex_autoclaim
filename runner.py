from proc import auth, reward
from time import sleep
from os import system

while 1:
    system("rm -rf res.txt")
    with open("data.txt", "r") as f:
        list = f.readlines()

    for i in range(len(list)):
        token = auth(list[i])
        sleep(0.5)
        code = reward(token)
        sleep(1)
        with open("res.txt", "a") as f:
            f.write(f" acc : {i+1} code : {code}\n")
    sleep(14400)
