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
  prCyan(print("Program Finished <3")
  PrGreen(print("Bangsat yang di temukan : found.txt")
  prYellow(print(" Raymond7 - Garuda Security Hacker")
 
