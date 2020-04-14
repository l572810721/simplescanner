import masscan
import os
import re
import argparse

def parse():
    parse = argparse.ArgumentParser(epilog="example:python3 masscan.py -ip 127.0.0.1")
    parse.add_argument("-ip",help="The host")
    return parse.parse_args()


def getport():
    hostport = []
    with open("result.txt","rb") as f:
        for port in f.readlines():
            port = port.decode()
            if port.startswith("<host endtime"):
                port = re.findall(r"portid=\"(.+?)\"",port)
                hostport.append("".join(port))
        f.close()
    return hostport

def scaner(ip):
    mscanpath = "./masscan/bin/masscan"
    cmd =mscanpath + " -sS --ports 0-65535 " + ip + " -oX result.txt --rate 3000"
    os.system(cmd)
    hostport = getport()
    print("\033[1;32;40m[+] The %s open port is : %s \033[0m" % (ip,",".join(hostport)))
    if(len(hostport)>20):
        print("The %s maybe hava firewall，Do you want to continue(y/n)?"%ip)
        flag = input(":")
        if(flag == "y"):
            pass
        else:
            exit()
    # nmapath = "./nmap/bin/nmap.exe"
    nmapcmd = "nmap -A -p " + ",".join(hostport) + " " + ip
    os.system(nmapcmd)

def main():
    args = parse()
    scaner(args.ip)

if __name__ == '__main__':
    main()