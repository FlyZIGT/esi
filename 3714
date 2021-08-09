import os
import time
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
    try:
        os.system('sudo cp esi.py /usr/bin/')
        destFile = home + r"/.bashrc"
    #wuith open(destFile, 'a') as f:
    #    f.write("the first appended text\r\n")
    #f.write("the second appended text\r\n")
    #f.write("the third appended text\r\n")
        fileName = home + r"/.bashrc"
        e = os.path.exists(fileName)
        if e == True:
            with open(destFile, 'a') as f:
                f.write('#esi\n')
                f.write('alias esi="python3 /usr/bin/esi.py"\n')
                f.write('#sesi\n')
        if e == False:
            os.system("sudo touch $HOME/.bashrc")
            with open(destFile, 'a') as f:
                f.write('#esi\n')
                f.write('alias esi="python3 /usr/bin/esi.py"\n')
                f.write('#sesi\n')
        except: 
            print('You need to be root to execute this script!')
            print('Exiting...')
            time.sleep(1)
            exit()
if s == "n":
    print('Exiting...')
    time.sleep(1)
    os.system('clear')
    exit()

print('Esi got Installed, type ise to execute the script!!')
print('Exiting...')
time.sleep(1)
exit()
