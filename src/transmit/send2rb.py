# Python Script to SEND Messages to RockBLOCK 9603

import sys
import requests
import binascii
from getpass import getpass

# RockBLOCK 9603 Device Serial Number and IMEI (Replace with your RockBLOCK device specfic information)
SN = "xxxxxx"
IMEI = "***************"

USERNAME = input("Enter your RockBLOCK Account Username: ")
if not USERNAME:
   raise Exception("RockBLOCK Username is required!!")
   sys.exit(1) 
print("Your RockBLOCK Account Username is:", USERNAME)

PASSWORD = getpass("Enter your RockBLOCK Account Password: ")
if not PASSWORD:
   raise Exception("RockBLOCK Account Password is required!!")
   sys.exit(1) 
print("Your RockBLOCK Account Password is:", PASSWORD)

msg = input("Enter your Message: ")
if not msg:
   raise Exception("A Message (to be sent to the RockBLOCK device) is required!!")
   sys.exit(1) 
print("Your Message to be sent to the RockBLOCK device is:", msg)

# encoded_msg = msg.encode("utf-8")
encoded_msg = msg.encode()

DATA = binascii.hexlify(encoded_msg)
print(DATA)
print(DATA.decode('utf-8'))
print("DATA Length: " + str(len(DATA.decode('utf-8'))))

# Build URL to HTTP POST send message
# url =https://core.rock7.com/rockblock/MT?imei=IMEI&username=USERNAME&password=PASSWORD&data=DATA
# base_url = "https://core.rock7.com/rockblock/MT?"
url = "https://core.rock7.com/rockblock/MT?imei={}&username={}&password={}&data={}".format(IMEI, USERNAME, PASSWORD, DATA.decode('utf-8'))
print(url)

print("Sending Message to ROCKBLOCK 9603 with IMEI: " + IMEI)
response = requests.post(url=url)
print(response)
