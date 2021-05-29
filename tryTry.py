import os, json

count_of_accounts = int(input("number: "))
accounts = []
x = 1

while x <= count_of_accounts:
    email = input("email: ")
    password = input("password: ")

    accounts.append({"email": email, "password": password})
    x += 1

data_code = [0, 0, accounts]

os.system("cd /storage/emulated/0/ && mkdir 'adro_gantiam' && cd /storage/emulated/0/adro_gantiam/ && mkdir 'AF' && cd /storage/emulated/0/adro_gantiam/AF/ && mkdir 1 && mkdir 2 && mkdir 3 && mkdir 4 && mkdir 5 && mkdir 6 && mkdir 7 && mkdir 8 && mkdir 9 && mkdir 10")

x = 1

while x != 11:
    worker_code = "import amino, os, json\nwith open('/storage/emulated/0/adro_gantiam/AF/data" + str(x) + ".txt') as json_file:\n    data = json.load(json_file)\nprint(str(data[0] + 1) + ': '+ str(data[1]))\nclient = amino.Client()\namino.lib.util.helpers.generate_device_info()\nclient.login(data[2][data[0]]['email'], data[2][data[0]]['password'])\nclient.join_community('188117165')\nsub_client = amino.SubClient('188117165', profile = client.profile)\nx = 0\nwhile x <= 12000:\n    print(sub_client.send_active_obj(x, x + 300))\n    x += 300\nclient.logout()\ndata[0] += 1\nwith open('/storage/emulated/0/adro_gantiam/AF/data" + str(x) + ".txt', 'w') as outfile:\n    json.dump(data, outfile)\nos.system('python py.py & rm device.json')" 

    open("/storage/emulated/0/adro_gantiam/AF/" + str(x) + "/py.py", "w").write(worker_code)
    with open("/storage/emulated/0/adro_gantiam/AF/data" + str(x) + ".txt", "w") as outfile:
        json.dump(data_code, outfile)

    x += 1

renew_code = 'import json\ndata = [0, 0, ' + str(accounts) + ']\nx = 1\nwhile x != 11:\n    with open("/storage/emulated/0/adro_gantiam/AF/data" + str(x) + ".txt", "w") as outfile:\n        json.dump(data, outfile)\n    x += 1' 

open("/storage/emulated/0/adro_gantiam/renew.py", "w").write(renew_code)
open("/storage/emulated/0/adro_gantiam/start.py", "w").write('import os\nos.system("cd /storage/emulated/0/adro_gantiam/AF/1/ && python py.py & cd /storage/emulated/0/adro_gantiam/AF/2/ && python py.py & cd /storage/emulated/0/adro_gantiam/AF/3/ && python py.py & cd /storage/emulated/0/adro_gantiam/AF/4/ && python py.py & cd /storage/emulated/0/adro_gantiam/AF/5/ && python py.py & cd /storage/emulated/0/adro_gantiam/AF/6/ && python py.py & cd /storage/emulated/0/adro_gantiam/AF/7/ && python py.py & cd /storage/emulated/0/adro_gantiam/AF/8/ && python py.py & cd /storage/emulated/0/adro_gantiam/AF/9/ && python py.py & cd /storage/emulated/0/adro_gantiam/AF/10/ && python py.py &")')

print("Successful")
print("Команда для сбора: cd /storage/emulated/0/adro_gantiam && python start.py")
print("Команда для скидания собирающего номера: cd /storage/emulated/0/adro_gantiam && python renew.py")
