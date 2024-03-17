###############################################################################################################
#                                                       |                      .____                          #
#                                                       |   ______ ____ ______ |    |    ____   ____  ______  #
#       Author        : Rux aka. RuxUnderscore          |  /  ___// ___\\____ \|    |   /  _ \ / ___\/  ___/  #
#       Email         : jonathan.e.rux@underscore.com   |  \___ \\  \___|  |_> >    |__(  <_> ) /_/  >___ \   #
#       Version       : 1                               | /____  >\___  >   __/|_______ \____/\___  /____  >  #
#       OS Support    : ALL                             |      \/     \/|__|           \/    /_____/     \/   #
#                                                       |     Secure Copy Logs from User Defined System       #
#                                                       |                                                     #
###############################################################################################################

import getpass, paramiko
from stat import S_ISDIR

paramiko.util.log_to_file("./tmp/paramiko.log")

# Get Target Systems Information from user.
def getClientInfo():
    host = input("Please enter the hostname or IP of the target system: ")
    user = input("Please enter the username for the target system: ")
    passwd = getpass.getpass(prompt=f"Please enter the password for {user}@{host}: ")
    return host, user, passwd
    
# Main Function
def main():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    host, user, passwd = getClientInfo()
    print(f"Using: {user}@{host}")
    client.connect(host, username=user, password=passwd)

# Decided to play with the if __name__ == "__main__" system.
if __name__ == "__main__":
    main()
