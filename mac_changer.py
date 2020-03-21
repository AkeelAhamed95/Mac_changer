# !/usr/bin/env python

import subprocess
import optparse 
import re

#this function allows us to acquire the Mac address and network interface (wifi card ethernet card) values from the Terminal, theses values are input by the user
def get_arguments():
    #for this we use the optparse module
     parser = optparse.OptionParser()
     #get the network interface device (WIFI card ethernet card)
     parser.add_option("-i", "--interface", dest="interface",  help="Interface to change its MAC address")
     #get the new MAC address
     parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
     
     #get the mac address and interface values
     (options, arguments) = parser.parse_args()
     
     #if no values were entered then show error messages
     if not options.interface:
            parser.error("[-] Please Specify an interface, use --help for more info.")
     elif not options.new_mac:
            parser.error("[-] Please Specify a new mac, use --help for more infor.")
     return options
       

#the function below changes the MAC address of the specified interface
def change_mac (interface, new_mac):
     print ("[+] Changing MAC address for " + interface + " to " + new_mac)
     #turn down the interface
     subprocess.call(["ifconfig", interface, "down"])
     #set the New mac address for the interface
     subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
     #turn the interface up
     subprocess.call(["ifconfig", interface, "up"])

#this function checks if the new mac address was set properly
def get_current_mac(interface):
      ifconfig_result = subprocess.check_output (["ifconfig", interface])
      #regular expression to read mac address from string
      mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w:", ifconfig_result)
     
      if mac_address_search_result: 
             return mac_address_search_result.group(0)
      else:
            print("[-] Could not read MAC address.")

options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac: 
       print("[+] MAC address was sucessfully changed to " + current_mac)
else:
       print("[-] MAC address did not got changed.")
       
change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface) 
if current_mac == options.new_mac: 
    print("[+] MAC address successfully changed to " + current_mac)
    
else: 
    print("[-] MAC address did not get changed.")

