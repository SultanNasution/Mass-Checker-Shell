#!/usr/bin/python
#Mass-Checker-Shell
#Bangsat2019
 # -*-coding:Latin-1 -*
import sys, requests
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
def prRed(prt): print("\033[91m {}\033[00m" .format(prt))
def prGreen(prt): print("\033[92m {}\033[00m" .format(prt))
def prYellow(prt): print("\033[93m {}\033[00m" .format(prt))
def prLightPurple(prt): print("\033[94m {}\033[00m" .format(prt))
def prPurple(prt): print("\033[95m {}\033[00m" .format(prt))
def prCyan(prt): print("\033[96m {}\033[00m" .format(prt))
def prLightGray(prt): print("\033[97m {}\033[00m" .format(prt))
def prBlack(prt): print("\033[98m {}\033[00m" .format(prt))

prCyan("_________ .__                   __                    _________.__           .__  .__     ")   
prCyan("\_   ___ \|  |__   ____   ____ |  | __ ___________   /   _____/|  |__   ____ |  | |  |    ")
prCyan("/    \  \/|  |  \_/ __ \_/ ___\|  |/ // __ \_  __ \  \_____  \ |  |  \_/ __ \|  | |  |    ")
prCyan("\     \___|   Y  \  ___/\  \___|    <\  ___/|  | \/  /        \|   Y  \  ___/|  |_|  |__  ")
prCyan(" \______  /___|  /\___  >\___  >__|_ \\___  >__|    /_______  /|___|  /\___  >____/____/  ")
prCyan("        \/     \/     \/     \/     \/    \/                \/      \/     \/             ")
print("")
prGreen(" Mass Checker Shell By Raymond7 - Garuda Security Hacker")
prGreen(" Thanks To : All Member Garuda Security Hacker")
prGreen(" Greezt : Mr.xBarakuda - ./Xi4u7 - ./Pierr0t's")
             
  
list = open(sys.argv[1], "r")
log = open("found.txt","a")
while True:
	ass = list.readline().repalce("\n","")
	if not ass:
		break
	abb = requests.get(ass, timeout=7)
	if abb.status_code == 200:
		print("Found Bangsat -> "+ass)
		log.write(ass+"\n")
	else:
		print("Bangsat Kabur :( -> "+ass)
