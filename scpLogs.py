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


from getpass import getpass
import paramiko

def getClientInfo():
    

def main():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    host, user, pass = getClientInfo()
    client.connect(host, username=$user, password=$pass)

if __name__ == "__main__":
    main()
