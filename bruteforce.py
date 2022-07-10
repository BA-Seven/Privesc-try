import os
import subprocess

print("[*] Beginning bruteforce using JohnTheRipper...\n")

os.system("john hashes.txt --format=NT --wordlist=wordlist.txt > /dev/null 2>&1")
output = subprocess.check_output("john hashes.txt --show --format=NT", shell=True)

print("[*] Bruteforce ended !")

output = output.decode("utf-8").split("\n")

# Removing useless lines
del output[len(output) - 1]
del output[len(output) - 1]
del output[len(output) - 1]

print("[i] Cracked creds :")
for i in output:
    hash = i.split(":")
    print(hash[0] + ":" + hash[1])
