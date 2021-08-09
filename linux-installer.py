import os
import time
from pathlib import Path
home = str(Path.home())
if os.geteuid() != 0:
    pass
else:
    print('To execute this script you need to be root.')
    time.sleep(0.1)
    print('Exiting...')
    time.sleep(2)

os.system('clear')
time.sleep(0.3)
os.system('figlet ISE  Set-up')
print("\n Dev: py#6650")
time.sleep(2)
print('Downloading all requirements...')
os.system('pip install colorama python-nmap')

os.system("clear")
s = input("Ise setup will add a command for easier use, do you want to add this command?\n y / n\n> ")
if s == "y":
    destFile = home + r"/.bashrc"
    #with open(destFile, 'a') as f:
    #    f.write("the first appended text\r\n")
    #f.write("the second appended text\r\n")
    #f.write("the third appended text\r\n")
    fileName = home + r"/.bashrc"
    e = True  #os.path.exists(fileName)
    if e == True:
        with open(destFile, 'a') as f:
            f.write('#esi\n')
            f.write('alias esi="python3 alias esi="python /data/data/com.termux/files/home/python/esi/esi.py""\n')
            f.write('#sesi\n')
    if e == False:
        os.system("sudo touch $HOME/.bashrc")
        with open(destFile, 'a') as f:
            f.write('#esi\n')
            f.write('alias esi="python3 /data/data/com.termux/files/home/python/esi/esi.py"\n')
            f.write('#sesi\n')
if s == "n":
    print('Exiting...')
    time.sleep(1)
    os.system('clear')
    exit()
#else:
#    print('Exiting...')
#    time.sleep(1)
#    os.system('clear')
#    exit()
os.system('source $HOME/.bashrc')
print('Esi got Installed, type ise to execute the script!!')
print('Exiting...')
time.sleep(1)
exit()
