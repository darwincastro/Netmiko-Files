from netmiko import ConnectHandler
import time

cisco = {
    "device_type": "cisco_ios",
    "host": "",
    "username": "",
    "password": "",
}

#open file to write the output of commands
file = open("output.txt", "a")


# output headers

firstheader = "--------------------- Before deauth --------------------\n"
secondheader = "--------------------- Show clock ----------------------\n"
thirdheader = "--------------------- After deauth ---------------------\n"

# Netmiko SSH Connection Handler

net_connect = ConnectHandler(**cisco)

status1 = net_connect.send_command("show wireless client mac-address <mac address> detail | i Session Timeout")
file.write(firstheader)
file.write(status1 + "\n\n")


deauth = net_connect.send_command("wireless client mac-address <mac address> deauthenticate")
file.write(deauth)

clock = net_connect.send_command("show clock")
file.write(secondheader)
file.write(clock + "\n\n")

# Sleep for 30 seconds

time.sleep(30)

status2 = net_connect.send_command("show wireless client mac-address <mac address> | i Session Timeout")
file.write(thirdheader)
file.write(status2 + "\n\n")

file.close()
