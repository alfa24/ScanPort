import socket

from platform import system as system_name  # Returns the system/OS name
from subprocess import call as system_call, DEVNULL  # Execute a shell command


def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Ping command count option as function of OS
    param = '-n' if system_name().lower() == 'windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    # Pinging
    return system_call(command,  stdout=DEVNULL) == 0


def get_hosts(host):
    ip = host.split(".")
    base_ip = "%s.%s.%s." % (ip[0], ip[1], ip[2])
    gbd = "10.248.168.82"
    analit = "10.248.168.14"
    if host[3] == "50" or host[3] == "52":
        trade = base_ip + "50"
        mail = base_ip + "52"
        printer = base_ip + "51"
        pos1 = base_ip + "3"
        pos2 = base_ip + "4"
        pos3 = base_ip + "5"
        fuel = base_ip + "6"
        kkm1 = base_ip + "18"
        kkm2 = base_ip + "19"
        kkm3 = base_ip + "20"
        bank1 = base_ip + "34"
        bank2 = base_ip + "35"
        bank3 = base_ip + "36"
    else:
        trade = base_ip + "178"
        mail = base_ip + "180"
        printer = base_ip + "179"
        pos1 = base_ip + "131"
        pos2 = base_ip + "132"
        pos3 = base_ip + "133"
        fuel = base_ip + "134"
        kkm1 = base_ip + "146"
        kkm2 = base_ip + "147"
        kkm3 = base_ip + "148"
        bank1 = base_ip + "162"
        bank2 = base_ip + "163"
        bank3 = base_ip + "164"

    hosts = [
        {"name": "GBD",
         "ip": gbd,
         "ports": [3389]},
        {"name": "Аналит. справка",
         "ip": analit,
         "ports": [80]},
        {"name": "Trade house",
         "ip": trade,
         "ports": [3389]},
        {"name": "Mail",
         "ip": mail,
         "ports": [3389]},
        {"name": "Printer",
         "ip": printer,
         "ports": [3389]},
        {"name": "Fuel",
         "ip": fuel,
         "ports": [3389]},
        {"name": "POS 1",
         "ip": pos1,
         "ports": [3389]},
        {"name": "POS 2",
         "ip": pos2,
         "ports": [3389]},
        {"name": "POS 3",
         "ip": pos3,
         "ports": [3389]},
        {"name": "KKT 1",
         "ip": kkm1,
         "ports": [3389]},
        {"name": "KKT 2",
         "ip": kkm2,
         "ports": [3389]},
        {"name": "KKT 3",
         "ip": kkm3,
         "ports": [3389]},
        {"name": "BANK 1",
         "ip": bank1,
         "ports": [3389]},
        {"name": "BANK 2",
         "ip": bank2,
         "ports": [3389]},
        {"name": "BANK 3",
         "ip": bank3,
         "ports": [3389]},
    ]
    return hosts

host = socket.gethostbyname(socket.getfqdn())
hosts = get_hosts(host)
print("--------------------------------")
print("Ожидайте идёт сканирование портов!")
print("--------------------------------")
for host in hosts:
    print("--------------------------------")
    print(host["name"] + " (" + host["ip"] + "):")
    print("     пингуем.......")
    print("     Пинг есть" if ping(host["ip"]) else "     Пинга нет")
    for port in host["ports"]:
        s = socket.socket()
        s.settimeout(1)
        try:
            s.connect((host["ip"], port))
        except socket.error:
            print("     " + str(port) + ' порт недоступен')
        else:
            s.close
            print("     " + str(port) + ' порт активен')
print("--------------------------------")
print("Процесс завершен")
