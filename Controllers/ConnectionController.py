import socket
import network

class ConnectionController():
    def __init__(self, ssid, password, ipAdress, port) -> None:
        self.ssid = ssid
        self.password = password
        self.ipAdress = ipAdress
        self.port = port


    
    def connect(self):

        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(self.ssid, self.password)

        ai = socket.getaddrinfo(self.ipAdress, self.port) # Address of Web Server
        addr = ai[0][-1]
        self.cl = socket.socket()
        self.cl.connect(addr)
        