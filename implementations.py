from netmiko import ConnectHandler
import re


def connect_network_device():
    network_devices = {"host": "127.0.0.1", "username": "", "password": "admin", "device_type": "cisco_ios",
                       "port": 10000}

    # Connecting to local server
    connect = ConnectHandler(**network_devices)

    # enable
    connect.enable()

    data = connect.send_command("show running-config")
    ip = re.findall("ip address (.*?)\n", data)
    desc = re.findall("\n description (.*?)\n", data)
    interface = re.findall("\ninterface (.*?)\n description", data)
    running_config = []
    for i in zip(ip, desc, interface):
        temp = {'interface': i[2], 'ip_address': i[0].split(" ")[0], 'subnet': i[0].split(" ")[1],
                'description': i[1]}
        running_config.append(temp)
    return running_config
