import socket
import network

class ConnectionController():
    def __init__(self, ssid, password) -> None:
        self.ssid = ssid
        self.password = password

        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(self.ssid, self.password)

        ai = socket.getaddrinfo("192.168.184.141", 1242) # Address of Web Server
        addr = ai[0][-1]
        self.cl = socket.socket() # Open socket
        self.cl.connect(addr)
        #"""