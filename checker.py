#!/usr/bin/python
#Mass-Checker-Shell
#Bangsat2019
 # -*-coding:Latin-1 -*
import sys, urllib2
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

 if __name__ == '__main__':
 
  print
  print
  print  

printcolored("prCyan", "_________ .__                   __                    _________.__           .__  .__     ")   
printcolored("prCyan", "\_   ___ \|  |__   ____   ____ |  | __ ___________   /   _____/|  |__   ____ |  | |  |    ")
printcolored("prCyan", "/    \  \/|  |  \_/ __ \_/ ___\|  |/ // __ \_  __ \  \_____  \ |  |  \_/ __ \|  | |  |    ")
printcolored("prCyan", "\     \___|   Y  \  ___/\  \___|    <\  ___/|  | \/  /        \|   Y  \  ___/|  |_|  |__  ")
printcolored("prCyan", " \______  /___|  /\___  >\___  >__|_ \\___  >__|    /_______  /|___|  /\___  >____/____/  ")
printcolored("prCyan", "        \/     \/     \/     \/     \/    \/                \/      \/     \/             ")
print
printcolored("prGreen", " Mass Checker Shell By Raymond7 - Garuda Security Hacker")
printcolored("prGreen", " Thanks To : All Member Garuda Security Hacker")
printcolored("prGreen", " Greezt : Mr.xBarakuda - ./Xi4u7 - ./Pierr0t's")
             
  
  
 
 
def cms(url):
 try:
 
   op =urllib2.urlopen(url,timeout=7)
   if "Upload" in op.read():
     prGreen( "Bangsat Ditemukan "+url)
     open("found.txt","a").write(url)

  
 except:
    prRed ( "Bangsat Menghilang"+ url)
    pass


def main():    
   
    for i in ListPass:
        try:
            i = i.strip()
            data=cms(i)
        except:
            pass
       
ListPass = open(sys.argv[1], 'r').readlines()      
pool = ThreadPool(250)
pool.map(cms, ListPass)
pool.close()
pool.join()
 
if __name__ == '__main__':     
 print
 print
 print
 
 printcolored("prCyan", "Program Finished Boy")
 printcolored("prGreen", "Bangsat yang di temukan : found.txt")
 printcolored("prYellow", " Raymond7 - Garuda Security Hacker")
 
